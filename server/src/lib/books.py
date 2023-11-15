import os
import logging

import lib.constants as CONST
import lib.google_api.google_api as google

from db.db import Database

db = Database()


def barcode_lookup(barcode, db_conn):
    # try to get book locally first
    query = """SELECT title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count
                    FROM book
                    WHERE upc = %(upc)s;
    """
    params = {
        'upc': barcode
    }
    local_books = db.read_db(db_conn, query, params)
    
    # get books from google if not found
    if not local_books:
        handler = google.factorio()
        books, err = handler.find_books(barcode)
        if err:
            return books, err
        books_added = add_books(books, db_conn)
        if not books_added:
            logging.error("Failed to add books")
        return books, err
        
    return local_books, None


def add_books(book_list, db_conn):
    # any time I fall back to google for search add or update record in db
    query = """INSERT IGNORE INTO book (title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count)
                VALUES (%(title)s, %(sub_title)s, %(authors)s, %(published_date)s, %(description)s, %(page_count)s, %(upc)s, %(thumbnail)s, %(count)s)
                ON DUPLICATE KEY UPDATE updated_at=CURRENT_TIMESTAMP;
    """

    return db.write_db(db_conn, query, book_list, multi_insert=True)


def query_lookup(query, db_conn):
    handler = google.factorio()
    books, err = handler.find_books(query)
    if err:
        return books, err
    books_added = add_books(books, db_conn)

    if not books_added:
        logging.error("Failed to add books")

    barcodes = [book['upc'] for book in books]
    local_books = get_books_by_barcode(db_conn, barcodes)
    if local_books:
        return local_books, None
    
    return books, err


def update_book_count(db_conn, barcode, count):
    query = """UPDATE book
                SET count = %(count)s
                WHERE upc = %(barcode)s"""
    params = {
        'count': count,
        'barcode': barcode
    }

    res = db.write_db(db_conn, query, params, get_update_row_count=True)
    if not res:
        return res, CONST.ERRORS['UPDATE_COUNT_FAIL']
    return res, None


def get_local_books(db_conn, order_by='updated_at', offset=0, limit=50):
    query = """SELECT title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count
                FROM book
                WHERE count >= 1
                ORDER BY %(order_by)s DESC
                LIMIT %(limit)s
                OFFSET %(offset)s;"""
    params = {
        'order_by': order_by,
        'limit': limit,
        'offset': offset
    }
    res = db.read_db(db_conn, query, params)
    if not res:
        return res, CONST.ERRORS['BOOKS_NOT_FOUND']
    return res, None


def get_books_by_barcode(db_conn, barcodes, order_by='udpated_at'):
    # this is so gross but I'm stumped, almost everything points back at an old as balls stack overflow answer that looks
    # twice as janks so I give up and do the ugly
    params = {
        'order_by': order_by
    }

    query_start = """SELECT title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count
                FROM book
                WHERE upc IN ("""
    
    for barcode in barcodes:
        query_start += f"%({barcode})s,"
        params[barcode] = barcode

    query_start = query_start[:-1]  
    query_end = """)
                ORDER BY %(order_by)s DESC;"""
    query = query_start + query_end
    return db.read_db(db_conn, query, params)
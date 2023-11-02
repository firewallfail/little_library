import os
import logging

import lib.constants as CONST
import lib.google_api.google_api as google

from db.db import Database

db = Database()


def barcode_lookup(barcode, db_conn):
    # try to get book locally first
    query = """SELECT title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count, updated_at
                    FROM book
                    WHERE upc = %(upc)s
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
            logging.error("Failed to add books", )
        return books, err
        
    return local_books, None


def add_books(book_list, db_conn):
    query = """INSERT INTO book (title, sub_title, authors, published_date, description, page_count, upc, thumbnail, count)
                VALUES (%(title)s, %(sub_title)s, %(authors)s, %(published_date)s, %(description)s, %(page_count)s, %(upc)s, %(thumbnail)s, %(count)s)
    """

    return db.write_db(db_conn, query, book_list, multi_insert=True)

import os
import logging

import lib.constants as CONST

from googleapiclient.discovery import build


def factorio():
    return googleBooks()


class googleBooks():

    def __init__(self):
        self.connection = build("books", "v1", developerKey=CONST.GOOGLE_API_KEY).volumes()

    def find_books(self, query):
        """Get books from google from search query or barcode

        Args:
            query (str): search query

        Returns:
            list: list of all books found and parsed
        """
        books = self.connection.list(q=query).execute()
        if not books or not len(books.get('items', [])):
            return [], CONST.ERRORS['BOOK_NOT_FOUND']
        
        return self.build_books_response(books['items']), False
    
    def build_books_response(self, book_list):
        """parse a list of books from google to match my db format

        Args:
            book_list (list): list of books from google

        Returns:
            list: list of parsed books
        """
        books = []
        for book in book_list:
            volume_info = book.get('volumeInfo', {})

            # skip any books that don't have an ISBN13 code
            upc = None
            for identifier in volume_info.get('industryIdentifiers', []):
                if identifier.get('type') == 'ISBN_13':
                    upc = identifier.get('identifier')
                    break
            if not upc:
                continue

            books.append({
                'title': volume_info.get('title'),
                'sub_title': volume_info.get('subtitle'),
                'authors': ', '.join(volume_info.get('authors', [])),
                'published_date': volume_info.get('publishedDate'),
                'description': volume_info.get('description'),
                'page_count': volume_info.get('pageCount'),
                'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail'),
                'count': 0,
                'upc': upc
            })
        return books
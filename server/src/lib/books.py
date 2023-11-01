import os
import logging

import lib.constants as CONST
import lib.google_api.google_api as google

from db.db import Database

db = Database()


def barcode_lookup(barcode):
    handler = google.factorio()
    return handler.find_books(barcode)


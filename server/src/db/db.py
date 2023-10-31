import logging
import json
import mysql.connector

import lib.constants as CONST

HOST = CONST.DB_HOSTNAME
USER = CONST.DB_USERNAME
PASSWORD = CONST.DB_PASSWORD
DATABASE = CONST.DB_DATABASE

class Database:

    def connect(self):
        try:
            return mysql.connector.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DATABASE)
        except Exception as e:
            logging.error(f"Exception creating db connection: {e}")

    def write_db(self, conn, query, params, get_update_row_count=False, auto_commit=True):
        try:
            with conn.cursor(buffered=True) as cur:
                cur.execute(query, params)
                if auto_commit:
                    conn.commit()
                result = cur.lastrowid
                if get_update_row_count:
                    result = cur.rowcount or CONST.NO_UPDATE_NEEDED
        except Exception as e:
            logging.error(f"Exception writing to db: {e}")
            return
        return result      

    def read_db(self, conn, query, params, only_one=False):
        try:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(query, params)
                if only_one:
                    result = cur.fetchone()
                else:
                    result = cur.fetchall()
            return result
        except Exception as e:
            logging.error(f"Exception reading from db: {e}")

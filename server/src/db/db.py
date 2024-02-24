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
        """Builds a connection to mysql db

        Returns:
            MySQLConnection: connection to db
        """
        try:
            return mysql.connector.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DATABASE)
        except Exception as e:
            logging.error(f"Exception creating db connection: {e}")

    def write_db(self, conn, query, params, get_update_row_count=False, auto_commit=True, multi_insert=False):
        """Writes to db

        Args:
            conn (MySQLConnection): connection to db
            query (str): sql query
            params (dict): params for query
            get_update_row_count (bool, optional): get number of rows updated on return. Defaults to False.
            auto_commit (bool, optional): commit query automatically. Defaults to True.
            multi_insert (bool, optional): handle multiple inserts. Defaults to False.

        Returns:
            int/cursor: an int indicating rows were inserted/updated or a cursor when manually commiting later
        """
        try:
            with conn.cursor(buffered=True) as cur:
                if multi_insert:
                    cur.executemany(query, params)
                else:
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
        """Reads from db 

        Args:
            conn (MySQLConnection): connection to db
            query (str): sql query
            params (dict): params for query
            only_one (bool, optional): flag to return a single row. Defaults to False.

        Returns:
            dict/list: results from query in a list of dicts or single row as dict
        """
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

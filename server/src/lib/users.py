import bcrypt
import logging
import uuid

from db.db import Database

db = Database()

def do_register(db_conn, creds):
    salt = bcrypt.gensalt(10)
    password = bytes(creds['password'], 'utf-8')
    passhash = bcrypt.hashpw(password, salt)

    query = """INSERT INTO user (public_id, email, username, password)
                VALUES(%(public_id)s, %(email)s, %(username)s, %(password)s)"""
    params = {
        "public_id": str(uuid.uuid4()),
        "email": creds.get('email', ''),
        "username": creds['username'],
        "password": passhash
        }

    result = db.write_db(db_conn, query, params)
    if result:
        return result


def do_login(db_conn, creds):
    query = """SELECT id, public_id, email, password, username, created_at
                FROM user
                WHERE username = %(username)s"""
    params = {
        "username": creds["username"]
    }

    result = db.read_db(db_conn, query, params, only_one=True)
    if not result:
        return
    
    password = result.pop('password')

    if bcrypt.checkpw(bytes(creds['password'], 'utf-8'), bytes(password, 'utf-8')):
        return result


def update_user(db_conn, public_id, creds):
    updatable_fields = ['username', 'email']
    params = {}
    for field in updatable_fields:
        if creds.get(field):
            params[field] = creds[field]
    update_fields = ','.join([f" {field}=%({field})s" for field in params])

    query = f"""UPDATE user
                  SET {update_fields}
                  WHERE public_id = %(public_id)s"""
    params['public_id'] = public_id
    
    return db.write_db(db_conn, query, params, get_update_row_count=True)


def update_user_password(db_conn, public_id, password):
    salt = bcrypt.gensalt(10)
    passhash = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
    query = """UPDATE user
                SET password = %(password)s
                WHERE public_id = %(public_id)s"""
    params = {
        'password': passhash,
        'public_id': public_id
    }
    return db.write_db(db_conn, query, params, get_update_row_count=True)


def delete_user(db_conn, public_id):
    query = """DELETE
                FROM user
                WHERE public_id = %(public_id)s"""
    params = {
        'public_id': public_id
    }
    return db.write_db(db_conn, query, params, get_update_row_count=True)



def get_user_by_id(db_conn, id):
    query = """SELECT public_id, email, username, created_at
                FROM user
                WHERE id = %(id)s"""
    params = {
        "id": id
    }

    return db.read_db(db_conn, query, params, only_one=True)


def get_user_by_public_id(db_conn, public_id):
    query = """SELECT id, public_id, email, username, created_at
                FROM user
                WHERE public_id = %(public_id)s"""
    params = {
        "public_id": public_id
    }

    return db.read_db(db_conn, query, params, only_one=True)

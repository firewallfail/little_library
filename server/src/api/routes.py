import json
import jwt
import logging

import api.helpers as helpers
import lib.constants as CONST
import lib.users as users
import lib.books as books

from flask import Blueprint
from flask import request
from flask import g
from flask import session

from api.helpers import token_required, required_params
from db.db import Database

api = Blueprint('api', __name__)
db = Database()

@api.errorhandler(Exception)
def server_error(err):
    logging.error(err)
    return helpers.failure(res='Generic server error', status_code=500)

@api.before_request
def before_request():
    query_params = request.args.copy() or {}
    body_params = request.get_json(silent=True) or {}
    form_params = request.form.copy() or {}
    file_params = request.files.copy() or {}
    g.params = {**query_params, **body_params, **form_params, **file_params}
    g.db_conn = db.connect()


@api.teardown_request
def teardown_request(res=''):
    if 'db_conn' in g and g.db_conn is not None:
        g.db_conn.close()


@api.route('/health_check')
def test():
    return helpers.success()


@api.route('/user/register', methods=['POST'])
def user_register():
    id = users.do_register(g.db_conn, g.params)
    if id:
        user = users.get_user_by_id(g.db_conn, id)
        user.pop('created_at')
        user['id'] = id
        token = helpers.build_token(user)
        session[token] = user.copy()
        user.pop('id')
        return helpers.success({'user': user, 'token': token})
    return helpers.failure()


@api.route('/user/login', methods=['POST'])
@required_params('username', 'password')
def user_login():
    logged = users.do_login(g.db_conn, g.params)
    if logged:
        logged.pop('created_at')
        token = helpers.build_token(logged)
        session[token] = logged.copy()
        logged.pop('id')
        return helpers.success({'user': logged, 'token': token})
    return helpers.failure()


@api.route('/user/logout')
def user_logout():
    token = request.headers.get('x-access-token')
    session.pop(token, default=None)
    return helpers.success()


@api.route('/user/update', methods=['PATCH'])
@token_required
def user_update():
    updated = users.update_user(g.db_conn, g.public_id, g.params)
    if updated:
        return helpers.success()
    return helpers.failure()


@api.route('/user/update-password', methods=['PATCH'])
@token_required
@required_params('username', 'password', 'new_password')
def user_update_password():
    matching_creds = users.do_login(g.db_conn, g.params)
    if not matching_creds:
        return helpers.failure(res="Update Password Error")
    updated = users.update_user_password(g.db_conn, g.public_id, g.params['new_password'])
    if updated:
        return helpers.success()
    return helpers.failure()


@api.route('/user/delete', methods=['DELETE'])
@token_required
def user_delete():
    deleted = users.delete_user(g.db_conn, g.public_id)
    if deleted:
        return helpers.success(res='user deleted')
    return helpers.failure(res='failed to delete user')


@api.route('/book/scan/<barcode>')
def get_book_from_barcode(barcode):
    book, err = books.barcode_lookup(barcode, g.db_conn)
    if not err:
        return helpers.success(book[0])
    return helpers.failure(res='failed to retrieve book', status=err)


@api.route('/book/search/<query>')
def get_book_from_query(query):
    return helpers.failure(res='failed to retrieve books')

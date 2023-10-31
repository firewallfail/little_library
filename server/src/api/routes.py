import json
import jwt
import logging

import api.helpers as helpers
import lib.constants as CONST

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


@api.route('/test')
def test():
    return helpers.success()
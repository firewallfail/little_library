import logging
import json
import jwt

from datetime import datetime, timedelta
from flask import Response
from flask import request
from flask import g
from flask import session
from functools import wraps

import lib.constants as CONST

SECRET_KEY = CONST.SECRET_KEY


def build_response(response, status="success", status_code=200):
    res = json.dumps({
        "status": status,
        "data": response
    }, default=str)
    return Response(res, mimetype="application/json", status=status_code)


def success(res="", status="success", status_code=200):
    return build_response(res, status=status, status_code=status_code)


def failure(res="", status="error", status_code=400):
    return build_response(res, status=status, status_code=status_code)


def build_token(user, expires_in_hours=24):
    exp = datetime.utcnow() + timedelta(hours=expires_in_hours)
    return jwt.encode(user, SECRET_KEY, 'HS256')


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token: # throw error if no token provided
            return failure(res='not authorized', status_code=401)
        try:
           # decode the token to obtain user public_id
            data = jwt.decode(token, CONST.SECRET_KEY, algorithms=['HS256'])
            g.public_id = data.get('public_id')
            user = session[token]
            if not user or user['public_id'] != data['public_id']:
                return failure(res='not authorized', status_code=401)
            g.user = user
        except:
            return failure(res='not authorized', status_code=401)
         # Return the user information attached to the token
        return f(*args, **kwargs)
    return decorator


def required_params(*required):
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            missing = [field for field in required if field not in g.params]
            if missing:
                return failure(f'missing fields: {missing}')
            return f(*args, **kwargs)
        return decorator
    return wrapper



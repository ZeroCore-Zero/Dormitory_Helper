from flask import Blueprint, jsonify, request, Response, make_response
from .utlis.response.response import empty_response
from .utlis.secrets import generate_token, verify_token
from .db import db, User
from buptmw import BUPT_Auth
from secrets import token_hex
from random import randint
from time import time


login = Blueprint('login', __name__)
secret_key = token_hex(16)


def login_verify():
    """ Verify login parameters with predefined types. """
    data = request.json
    login_opt = data.get('login_opt')
    username = data.get('username')
    password = data.get('password')
    stay_login_in = data.get('stay_login_in')

    if login_opt not in ["default", "bupt_net_login"]:
        return False
    if not isinstance(username, str) or len(username) == 0:
        return False
    if not isinstance(password, str) or len(password) == 0:
        return False
    if stay_login_in not in [True, False]:
        return False
    return True


def login_unpd(username, password):
    """ Login with username and password. """
    result = User.query.filter_by(username=username, password=password).first()
    return result


def login_bupt(buptid, password):
    """ Login with BUPT CAS. """
    bupt_user = BUPT_Auth(cas={"username": buptid, "password": password})
    if bupt_user.cas.status is False:
        return None
    
    result = User.query.filter_by(BUPTID=buptid).first()
    is_new = False
    if result is None:
        if_new = True
        # if new user, create user in database.
        username = f"bupt#{randint(1000, 9999)}"
        while User.query.filter_by(username=username).first() is not None:
            username = f"{buptid}#{randint(1000, 9999)}"
        email = f"{buptid}@bupt.edu.cn"
        name = bupt_user.get_UC().name

        result = User(username=username, password=password, email=email, name=name, BUPTID=buptid)
        db.session.add(result)
        db.session.commit()
    return result, is_new


@login.route('/auth/login', methods=['POST'])
def login_fun():
    # get data and verify format
    if not login_verify():
        return empty_response(400)
    data = request.json
    login_opt = data.get('login_opt')
    username = data.get('username')
    password = data.get('password')
    stay_login_in = data.get('stay_login_in')

    # query user info
    is_new = False
    if login_opt == "default":
        result = login_unpd(username, password)
    elif login_opt == "bupt_net_login":
        result, is_new = login_bupt(username, password)
    else:
        return empty_response(422)


    # if result is a Response, then return directly.
    # else generate token.
    if isinstance(result, Response):
        return result
    if result is None:
        return empty_response(401)
    payload = {
        "username": result.username,
        "email": result.email
    }
    token = generate_token(payload, secret_key)

    respdata = {
        "token": token,
        "is_new": is_new
    }
    return jsonify(respdata)

from flask import Blueprint, jsonify, request
from .utlis.response.response import empty_response
from .utlis.secrets import generate_token, verify_token
from .db import User
from buptmw import BUPT_Auth
from secrets import token_hex


login = Blueprint('login', __name__)
secret_key = {}


def login_verify():
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


@login.route('/auth/login', methods=['POST'])
def login_fun():
    # get data and verify format
    if not login_verify():
        return empty_response(401)
    data = request.json
    login_opt = data.get('login_opt')
    username = data.get('username')
    password = data.get('password')
    stay_login_in = data.get('stay_login_in')

    # query user info
    if login_opt == "default":
        result = User.query.filter_by(username=username, password=password).first()
    elif login_opt == "bupt_net_login":
        result = User.query.filter_by(BUPTID=username).first()
    else:
        return empty_response(422)

    # special handling for bupt login
    if login_opt == "bupt_net_login" and result is None:
        bupt_user = BUPT_Auth(cas={"username": username, "password": password})
        if bupt_user.cas.status is False:
            return empty_response(401)

    # generate token
    if result is None:
        return empty_response(401)
    payload = {
        "username": result.username,
        "email": result.email
    }
    secret_key[username] = token_hex(16)
    token = generate_token(payload, secret_key[username])

    return jsonify({"token": token})

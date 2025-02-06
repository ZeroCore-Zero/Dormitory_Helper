import jwt


def generate_token(payload, secret_key, algorithm='HS256'):
    token = jwt.encode(payload, secret_key, algorithm)
    return token


def verify_token(token, secret_key, algorithms=['HS256']):
    try:
        payload = jwt.decode(token, secret_key, algorithms)
    except jwt.ExpiredSignatureError:
        return [False]
    except jwt.InvalidTokenError:
        return [False]
    else:
        return [True, payload]

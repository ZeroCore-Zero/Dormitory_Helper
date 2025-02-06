from flask import make_response


def empty_response(code):
    return make_response('', code)

import re
from functools import wraps, partial
from flask import request, make_response, jsonify


def verify_email(email):
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if email_regex.match(email):
        return True
    return False


def validate_json_header(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.json:
            """   request.json
           except BadRequest as e:"""
            return make_response(jsonify(
                "Oops! That didn't work\
                Please provide a valid json header\t")), 400
        return f(*args, **kwargs)
    return wrapper


"""
def verify_email(f, email):
    @wraps(f)
    def wrapper(*args, **kwargs):
        email_regex = re.compile(r"[^@\\s]+@[^@\\s]+\\.[a-zA-Z0-9]+$")

        if email_regex.match(email):
            return f(*args, **kwargs)
        else:
            return make_response(jsonify("Email format unkown")), 400
    return wrapper


real_email = partial(verify_email)
"""

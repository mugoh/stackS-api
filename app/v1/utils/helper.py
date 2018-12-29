import re
from functools import wraps
from flask import request, make_response, jsonify
from werkzeug.exceptions import BadRequest


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

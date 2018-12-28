import re


def verify_email(email):
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
    return email_regex.match(email)

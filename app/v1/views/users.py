from flask import Blueprint, request, make_response, jsonify, session
import random
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.v1.utils.helper import verify_email, validate_json_header
from app.v1.models.users import UserModel

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth/')

blacklisted_tokens = set()


@auth.route('register', methods=['POST', 'GET'])
@validate_json_header
def register_user():
    """
    Registers new users and returns a list of
    all registered users

    """
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')

        if verify_email(email) and len(password) > 6:

            if UserModel.get_by_email(email):
                return make_response(jsonify(
                    "Account exists. Maybe log in?")), 409
            if UserModel.get_by_name(username):
                return make_response((jsonify(
                    "Oopsy!Username exists", "Try ",
                    username + str(random.randint(0, 20))))), 409

            UserModel(username=username,
                      email=email,
                      password=password).save()

            return make_response(jsonify({
                "Status": "Success"
            })), 201

        # For incorrect user details
        return make_response(jsonify(
            "\nPlease Provide a valid email.\
            \nEnsure password is has at least 5 characters\nCool?")), 400

    return make_response(jsonify(UserModel.get_all_users()))


@auth.route('login', methods=['POST'])
@validate_json_header
def login_user():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')
    username = data.get('username')

    if not verify_email(email):
        return make_response(jsonify(
            "Please Provide a valid email. Cool?")), 400

    user = UserModel.get_by_email(email)

    if not user:
        return make_response(jsonify({
            "Status": "Fail",
            'msg': "Account not known. Maybe register?"})), 400
    elif not user.check_password(password):
        return make_response(jsonify(
            "Incorrect password. Please give me the right thing, okay?")), 400
    user_token = create_access_token(identity=username)

    session['logged_in'] = True

    return make_response(jsonify({
        "Status": "Success",
        "Logged in as": repr(user),
        "Token": user_token
    })), 201


@auth.route('logout', methods=['DELETE'])
@validate_json_header
def logout_user():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return make_response(jsonify(
            "Missing an email")), 400
    jti = get_raw_jti()['jti']

    blacklisted_tokens.add(jti)
    return make_response(jsonify(
        "Logout successful")), 201

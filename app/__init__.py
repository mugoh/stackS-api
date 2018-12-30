from flask import Flask
from app.v1.views.users import auth, blacklisted_tokens
from instance.config import APP_CONFIG
from flask_jwt_extended import JWTManager


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

    jwt = JWTManager(app)
    app.config.from_object(APP_CONFIG[
        config_setting.strip().lower()])

    @jwt.token_in_blacklist_loader
    def check_blacklisted_token(token):
        jti = token['jti']
        return jti in blacklisted_tokens

    return app

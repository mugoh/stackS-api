from flask import Flask
from app.v1.views.users import auth
from instance.config import APP_CONFIG
from flask_jwt_extended import JWTManager


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth)
    jwt = JWTManager(app)
    app.config.from_object(APP_CONFIG[
        config_setting.strip().lower()])

    return app

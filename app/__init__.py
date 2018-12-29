from flask import Flask
from app.v1.views.users import auth
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.config.from_object(APP_CONFIG[
        config_setting])

    return app

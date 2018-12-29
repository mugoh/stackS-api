from flask import Flask
from v1.views.users import auth
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth)

    app.config_from_object(APP_CONFIG[
        config_setting.strip().lower()])

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    
    from .users import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    from .utilities import utility as utility_blueprint
    app.register_blueprint(utility_blueprint)
    
    return app
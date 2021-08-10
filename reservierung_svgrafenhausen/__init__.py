from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists

SERVER = True

db = SQLAlchemy()
DB_NAME = "database.db"

if SERVER:
    DB_PATH = f"/home/{DB_NAME}"
else:
    DB_PATH = f"/tmp/{DB_NAME}"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Das darfst du nicht wissen xD'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        db.create_all(app=app)
        print('Created Database!')

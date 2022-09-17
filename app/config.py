from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv, path
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import func, or_, String
from werkzeug.middleware.proxy_fix import ProxyFix


basedir = path.abspath(path.dirname(__file__))
db = SQLAlchemy()
migrate = Migrate()
admin = Admin()
per_page = 5


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    app.secret_key = str(getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL", "postgresql://")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    return app

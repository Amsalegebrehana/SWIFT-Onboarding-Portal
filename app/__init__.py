from flask import Flask, render_template, request, json, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # Configure MariaDB database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Amsa1e-Ge@localhost:3306/swifttest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "hello"
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import main

    app.register_blueprint(main)

    from . import models
    
    return app
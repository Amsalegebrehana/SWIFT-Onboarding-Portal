from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# ... database configuration
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    company_name = db.Column(db.String(120), nullable=False)
    company_size = db.Column(db.String(40), nullable=False)

class Request(db.Model):

    __tablename__ = 'request'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    connection_type = db.Column(db.String(40), nullable=False)
    services = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    assigned_account_manager = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    verification_notes = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)

class Admin(db.Model):

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role_level = db.Column(db.String(40), nullable=False)
    skills = db.Column(db.String(200), nullable=False)
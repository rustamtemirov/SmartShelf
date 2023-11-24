from flask_sqlalchemy import SQLAlchemy
from app import db

<<<<<<< HEAD
class User(db.model):
=======
class User(db.Model):
>>>>>>> 3d36a0c648f6d7140b38dc2624a89bb08e642c04
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
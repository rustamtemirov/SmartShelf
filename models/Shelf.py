from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shelf(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    products = db.relationship('Product', backref='shelf', lazy=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Shelf('{self.name}')"
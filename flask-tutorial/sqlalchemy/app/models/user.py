from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.create_all()
class User(db.Model):
    id = db.column(db.Integer,primary_key=True)
    name = db.column(db.String(100),nullable=False)
    email = db.column(db.String(200),unique=True)
    posts = db.relationship('Post',backref='author',lazy=True)
# Standard imports

# Third party imports

# Custom imports
from src.main import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(2000))

class Info(db.Model):
    __tablename__ = 'Info'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(2000))

class Insults(db.Model):
    __tablename__ = 'Insults'
    id = db.Column(db.Integer, primary_key=True)
    insult = db.Column(db.String(5000))
    user = db.Column(db.String(50))

class Funfacts(db.Model):
    __tablename__ = 'Facts'
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(5000))

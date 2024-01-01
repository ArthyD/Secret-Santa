
from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(150))
    password = db.Column(db.String(150))
    est_admin = db.Column(db.Boolean)

class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom= db.Column(db.String(150))
    hash = db.Column(db.String(150))
    found = db.Column(db.Boolean)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

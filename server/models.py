# Attention! Migration does not provide enums on downgrade (PostgreSQL 9.6). Do it manually.
# https://stackoverflow.com/questions/37848815/sqlalchemy-postgresql-enum-does-not-create-type-on-db-migrate

from application import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    language = db.Column(db.Enum('english', 'russian', name='language'), nullable = False, server_default = 'english')

class Pill(db.Model):
    __tablename__ = 'pills'

    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.ForeignKey("users.id"))
    name = db.Column(db.String(255), nullable = False)
    unit = db.Column(db.Enum('pieces', 'mg', 'ml', name='unit'))
    dosage = db.Column(db.Integer)
    intake = db.Column(db.Enum('before', 'during', 'after', name='intake'))
    startdate = db.Column(db.Date, nullable = False)
    enddate = db.Column(db.Date, nullable = False)
    days = db.Column(db.SmallInteger)
    times = db.Column(db.Time, nullable = False)

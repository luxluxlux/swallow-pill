# Attention! Migration does not provide enums on downgrade (PostgreSQL 9.6). Do it manually.
# https://stackoverflow.com/questions/37848815/sqlalchemy-postgresql-enum-does-not-create-type-on-db-migrate

import enum
from application import db


class Language(enum.Enum):
    english = 'english'
    russian = 'russian'


class Unit(enum.Enum):
    pieces = 'pieces'
    mg = 'mg'
    ml = 'ml'


class Intake(enum.Enum):
    before = 'before'
    during = 'during'
    after = 'after'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    language = db.Column(db.Enum(Language), nullable=False,
                         server_default=str(Language.english.value))


class Pill(db.Model):
    __tablename__ = 'pills'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.ForeignKey("users.id"))
    name = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.Enum(Unit))
    dosage = db.Column(db.Integer)
    intake = db.Column(db.Enum(Intake))
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)
    days = db.Column(db.ARRAY(db.SmallInteger))
    times = db.Column(db.ARRAY(db.Time), nullable=False)

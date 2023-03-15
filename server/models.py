from app import db

class Language(db.Enum):
    english = 'english',
    russian = 'russian'

class Unit(db.Enum):
    pieces = 'pieces',
    mg = 'mg',
    ml = 'ml'

class Intake(db.Enum):
    before = 'before',
    during = 'during',
    after = 'after'

class User(db.Model):
    __tablename__ = 'users'

    # TODO Create sequence
    # TODO May need an UUID
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    language = db.Column(Language, nullable = False, default = Language.english)

class Pill(db.Model):
    __tablename__ = 'pills'

    # TODO Create sequence
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.ForeignKey("users.id"))
    unit = db.Column(Unit)
    dosage = db.Column(db.Integer)
    intake = db.Column(Intake)
    startdate = db.Column(db.Date, nullable = False)
    enddate = db.Column(db.Date, nullable = False)
    days = db.Column(db.SmallInteger)
    times = db.Column(db.Time, nullable = False)

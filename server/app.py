from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create app
app = Flask(__name__, static_url_path='', static_folder='../client/build', template_folder='../client/build')

# Load configuration
app.config.from_pyfile("configuration.py")

# initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes, models

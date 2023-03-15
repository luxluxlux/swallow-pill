from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='../client/build', template_folder='../client/build')

    # Load configuration
    app.config.from_pyfile("configuration.py")

    # initialize database
    db.init_app(app)
    Migrate(app, db)

    # Import database models
    import models

    # Register blueprints
    from routes import routes
    app.register_blueprint(routes)

    return app

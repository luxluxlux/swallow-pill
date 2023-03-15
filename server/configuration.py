# Environment variables can be set in the shell before starting the server
# Windows: $env:NAME = "value"
# Linux, MacOS: export NAME="value"

import os

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DATABASE_NAME}"
)

import os

# TODO Return after test
# DB_USERNAME = os.environ["DB_USERNAME"]
# DB_PASSWORD = os.environ["DB_PASSWORD"]
# DB_HOST = os.environ["DB_HOST"]
# DATABASE_NAME = os.environ["DATABASE_NAME"]

DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DATABASE_NAME = "spdb"
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DATABASE_NAME}"
)

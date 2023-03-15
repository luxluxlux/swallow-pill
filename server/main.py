import os, sys
from app import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

if __name__ == "__main__":
    # TODO Add debug mode
    # https://habr.com/ru/post/193242/
    app.run()

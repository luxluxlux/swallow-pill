from flask import Flask, render_template
from configuration import get_configuration
from database import connect_to_database

app = Flask(__name__, static_url_path='', static_folder='../client/build', template_folder='../client/build')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    configuration = get_configuration()
    connect_to_database(configuration['database'])
    app.run()
    
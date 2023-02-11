from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='', static_folder='../client/build')

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())
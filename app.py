import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    users = {
        0: "John Doe",
        1: "Mark Hamill",
        2: "Michael Jordan",
    }
    return render_template('index.html', users=users)
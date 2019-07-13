from flask import Flask, render_template
from settings import NAME

app = Flask(__name__)

@app.route('/')
def hello():
#     return f"Hello, {NAME}"
    return render_template("index.html", name=NAME)

@app.route('/numbertwo')
def second_route():
    return render_template("numbertwo.html")

@app.route('/test')
def test_route():
    return render_template("test1.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5'])
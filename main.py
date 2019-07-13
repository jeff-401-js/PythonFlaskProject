from flask import Flask, render_template
from settings import NAME

app = Flask(__name__)

@app.route('/')
def hello():
#     return f"Hello, {NAME}"
    return render_template("hello.html", name=NAME)

@app.route('/numbertwo')
def second_route():
    return render_template("numbertwo.html")
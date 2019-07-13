from flask import Flask, render_template
# from settings import NAME

app = Flask(__name__)

@app.route('/')
def hello():
#     return f"Hello, {NAME}"
    return render_template("index.html")

@app.route('/sales')
def second_route():
    return render_template("sales.html")


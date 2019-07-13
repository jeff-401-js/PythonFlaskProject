from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
import json

client = MongoClient(f"{MONGO}")
db = client.tempDB

app = Flask(__name__)

@app.route("/")
def hello():
#     return f"Hello, {NAME}"
    return render_template("index.html")

@app.route("/sales")
def second_route():
    return render_template("sales.html")

@app.route("/post", methods = ['POST'])
def add_store_sales():
    data = json.loads(request.data)
    name = data["name"]
    minimum = data["minimum"]
    maximum = data["maximum"]
    average = data["average"]

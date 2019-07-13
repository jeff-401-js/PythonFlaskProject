from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost:27017')
db = client.ContactDB

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
    try:
        data = json.loads(request.data)
        name = data["name"]
        minimum = data["minimum"]
        maximum = data["maximum"]
        average = data["average"]
        if name and minimum and maximum and average:
          status = db.Contacts.insert_one({
            "name" : name,
            "minimum" : minimum,
            "maximum" : maximum,
            "average" : average
          })
        return dumps({ 'message' : 'SUCCESS'})
    except Exception:
        return dumps({ 'error'})

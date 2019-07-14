from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS
import json

client = MongoClient('localhost:27017')
db = client.CookieDB

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sales")
def second_route():
    return render_template("sales.html")

# @app.route("/post", methods = ['POST'])
# def add_store_sales():
#     try:
#         # data = json.loads(request.data)

#         name = request.form["name"]
#         minimum = request.form["minimum"]
#         maximum = request.form["maximum"]
#         average = request.form["average"]
#         if name and minimum and maximum and average:
#           db.Cookies.insert_one({
#             "name" : name,
#             "minimum" : minimum,
#             "maximum" : maximum,
#             "average" : average
#           })
#         return dumps({ 'message' : 'SUCCESS'})
#     except Exception:
#         return dumps({ 'error' : 'post no good'})

# @app.route("/get", methods = ['GET'])
# def get_store_sales():
#     try:
#         salesData = db.Cookies.find()
#         # for sale in salesData:
#         print(salesData)
#         return render_template("sales.html", sales={salesData})
#     except Exception:
#         return dumps({ 'error' : 'get no good'})
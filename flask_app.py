
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json
import numpy
import pandas as pd
import sys
from stockxsdk import Stockx
stockx = Stockx()

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="KevTLy",
#     password="fluffykins123",
#     hostname="KevTLy.mysql.pythonanywhere-services.com",
#     databasename="KevTLy$comments",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class Comment(db.Model):

#     __tablename__ = "comments"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(4096))

# comments = []

# @app.route("/")
@app.route("/", methods=["GET", "POST"])
@cross_origin()
def searchStockx():
    if request.method == 'POST':
        searchText = request.data
        print(searchText)
        searchRes = jsonify(stockx.search(searchText))
        print(searchRes)
        return searchRes
    return jsonify('GET instead')

# @app.route("/", methods=["GET"])
# @cross_origin()
# def stockx_get():
#     return jsonify('in GET request')

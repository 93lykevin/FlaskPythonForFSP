
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

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="KevTLy",
    password="fluffykins123",
    hostname="KevTLy.mysql.pythonanywhere-services.com",
    databasename="KevTLy$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# comments = []

# @app.route("/")
@app.route("/", methods=["GET", "POST"])
@cross_origin()
def stockx_search():
    supreme = jsonify(stockx.search('Supreme'))

    # supreme.headers.add('Access-Control-Allow-Origin', '*')
    return supreme

    # return request.post('

    # supreme = pd.DataFrame(supreme)
    # return jsonify(supreme.head())
# def index():
#     if request.method == "GET":
#         # return render_template("main_page.html", comments=Comment.query.all())

# comment = Comment(content=request.form["contents"])
#     db.session.add(comment)
#     db.session.commit()
#     return redirect(url_for('index'))
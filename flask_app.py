
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import numpy
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please be easy to use'


# This is a basic REST micro service example for python using the flask library
# Docs: http://flask.pocoo.org/docs/1.0/
import re

from flask import Flask

app = Flask(__name__)


# -----------------------------------------------------
# Basic 'customer' example for REST like resource paths
# -----------------------------------------------------


@app.route('/', methods=['GET'])
def index():
    return 'DPNB Microservice Demonstrator'


import time
from flask import Flask
import pandas as pd
import sys


#print(time.altzone)

application = Flask(__name__)
@application.route('/')
def hello_world():
    return "Subscribe"






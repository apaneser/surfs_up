# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up database
engine = create_engine('sqlite:///hawaii.sqlite')

# reflect the tables
Base = automap_base
Base.prepare(engine, reflect=True)

# store classes into variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link
session = Session(engine)

# new Flask App instance
app = Flask(__name__)

# create root route
@app.route('/')
def hello_world():
    return 'Hello World'



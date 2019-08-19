from flask import Flask, request, jsonify, render_template, redirect
import os
import json
#Flask 
import numpy as np
import pandas as pd
from pandas import *
import datetime as dt
from datetime import timedelta, datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
from citipy import citipy

engine = create_engine("sqlite:///desktop/ETL-Allergy-Free/restaurant_ratings.db")
conn= engine.connect()
data = pd.read_sql("SELECT * FROM restaurants", conn)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()
# Save references to each table
Restaurants= Base.classes.restaurants
session = Session(engine)
    

app = Flask(__name__)

@app.route('/Restaurants')
def index():
    df = session.query(Restaurants.name, Restaurants.city, Restaurants.food_rating).all()
    df = pd.DataFrame(df, columns=['Restaurant Name', 'City','Allergy-Friendly Rating'])
    myhtml=df.to_html()     

    return render_template('index.html', table='allresttable.html')

    # run Flask app
    if __name__ == "__main__":
        app.run()
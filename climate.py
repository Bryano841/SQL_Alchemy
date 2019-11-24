import numpy as numpy
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///C:/Users/bryan_j7mwyoj/Desktop/Class repo/10-Advanced-Data-Storage-and-Retrieval/Homework/Instructions/hawaii.sqlite",
    connect_args={'check_same_thread': False})

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

last12 = session.query(Measurement.date).order_by(Measurement.date.desc()).first())
last12 = list(np.ravel(last12))[0]
last12 = dt.datetime.strptime(last12, '%Y-%m-%d')
lastYear = int(datetime.strftime(last12, '%Y'))
lastMonth = int(datetime.strftime(last12, '%m'))
lastDay = int(datetime.strftime(last12, '%d'))

prevYear = dt.date(lastYear, lastMonth, lastDay)-dt.timedelta(days=365)
prevYear = dt.datetime.strftime(prevYear, '%Y-%m-%d')

@app.route("/")
def home():
    return (f"Welcome to Hawaii Climate API <br/>"
    "Available Routes:<br/>"
    f"/api/stations<br/>"
    f"/api/precipitation<br/>"
    f"/api/temperature<br/>"
    f"datesearch (yyyy-mm-dd)")

@app.route("/api/stations")
    def stations():
        results = session.query(Station.name).all()
        all_stats = list(np.ravel(results))
        return jsonify(all_stats)

@app.route("/api/precipitation")
    def precipitation():
        results = (session.query(Measurement.date, Measurement.prcp,
        Measurement.station).filter(Measurement.date > prevYear)
        order_by(Measurement.date).all())
prcpData = []
    for result in results:
        prcpDict = {result.date: result.prcp, "Station": result.station}
        prcpData.append(prcpDict)
    return jsonify(prcpData)

    @app.route("/api/temperature")
        def temperature():
            results = session.query(Measurement.date, Measurement.tobs, Measurement.station)
                            .filter(Measurement.date > prevYear)
                            .order_by(Measurement.date)
                            .all())

@app.route("/api/temperature")
def temperature():
    results = (session.query(Measurement.date, Measurement.tobs, Measurement.station)
                .filter(Measurement.date > prevYear)
                .order_by(Measurement.date)
                .all())

tempData= []
for results in results:
    tempDict = {result.date: result.tobs, "Station": result.station}
    tempData.append(tempDict)

@app.route("/api/datesearch/<startDate>")
def start(startDate):
    for result in results:
        date_dict = {}
        date_dict["Date"] = result [0]
        date_dict["Low Temp"] = result[1]
        date_dict["Avg Temp"]= result[2]
        date_dict["High Temp"] = result[3]
        dates.append(date_dict)
        return jsonify (dates)

@app.route('/api/datesearch/<startDate>/<endDate>')
def startEnd(startDate, endDate):
    sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    results = (session.query(*sel)
                .filter(func.strftime("%Y-%m-%d", Measurement.date)>= startDate)
                .filter(func.strftime("%Y-%m-%d", Measurement.date<= endDate)
                .group_by(Measurement.date)
                .all())

date=[]
for result in results:
    date_dict{}
    date_dict["Date"]= result[0]
    date_dict["Low Temp"]= result[1]
    date_dict["Avg Temp"]= result[2]
    date_dict["High Temp"]= result[3]
    dates.append(date_dict)
return jsonify(dates)

if __name__ == "__main__":
    app.run(debug=True)
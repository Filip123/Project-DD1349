from app import app

import app.src.visualCar as visualCar
import app.src.databaseAccess as databaseAccess
from flask import jsonify, render_template, request

#Home page
@app.route("/")
def index():
    session_country_list = databaseAccess.fetch_session_data()
    return render_template("mainPage.html", session_country_list=session_country_list)

@app.route("/get-coordinates")
def get_coordinates():
    
    currentTime = request.args.get('currentTime', 0)
    currentSession = request.args.get('currentSession', 9165)
    print(currentTime)
    print(currentSession)
    #Here issue
    coordinateList = visualCar.getPositionsOverTimeInterval(int(currentSession), 1, currentTime, 10)
    return jsonify(coordinateList)   

@app.route("/get-country")
def get_country():
    sessionKey = request.args.get('sessionKey', 0)
    countryName = databaseAccess.fetch_country_name(sessionKey)
    return countryName

@app.route("/get-startTime")
def get_startTime():
    sessionKey = request.args.get('sessionKey', 0)
    startTime = databaseAccess.fetch_start_time(sessionKey)
    return '2023-09-17T13:00:00' #Should be starttime


def movebackwards():
    pass

@app.route("/get-racetrack-coordinates")
def get_racetrack_coordinates():
    raceStartTime = request.args.get('raceStart', 0)
    print("yooooo")
    coordinateList = visualCar.getPositionsOverTimeInterval(9165, 4, raceStartTime, 500)
    return jsonify(coordinateList)
  
@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
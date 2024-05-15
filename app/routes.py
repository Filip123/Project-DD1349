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
    print(currentTime)
    coordinateList = visualCar.getPositionsOverTimeInterval(9165, 4, currentTime, 10)
    return jsonify(coordinateList)   

@app.route("/get-country")
def get_country():
    sessionKey = request.args.get('sessionKey', 0)
    countryName = databaseAccess.fetch_country_name(sessionKey)
    return countryName


def movebackwards():
    pass
  
@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
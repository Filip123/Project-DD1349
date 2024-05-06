from app import app
import visualCar
from flask import jsonify, render_template, request

#Home page
@app.route("/")
def index():
    return render_template("mainPage.html")

@app.route("/get-coordinates")
def get_coordinates():
    currentTime = request.args.get('currentTime', 0)
    print(currentTime)
    print("working???")
    coordinateList = visualCar.getPositionsOverTimeInterval(9165, 1, currentTime, 5)
    return jsonify(coordinateList)   

def movebackwards():
    pass
  
@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
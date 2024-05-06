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
    #coordinateList = [[186, 6294], [178, 6622], [169, 6967], [158, 7289], [143, 7685], [131, 7899], [113, 8063], [49, 8246], [1, 8299], [63, 8337]]
    coordinateList = visualCar.getPositionsOverTimeInterval(7953, 1, currentTime, 10)
    return jsonify(coordinateList)   

def movebackwards():
    pass
  
@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
from app import app
from flask import jsonify, render_template

#Home page
@app.route("/")
def index():
    return render_template("mainPage.html")

@app.route("/get-coordinates")
def get_coordinates():
    coordinateList = [[6422, 5580], [6386, 5549], [6244, 5416], [6184, 5353], [6071, 5220], [6007, 5138], [5907, 4997], [5842, 4898], [5787, 4808], [5691, 4649], [5640, 4573], [5538, 4448], [5424, 4343], [5358, 4296], [5263, 4245], [5189, 4218], [5002, 4187], [4920, 4185], [4827, 4186], [4776, 4187], [4630, 4190], [4501, 4187], [4382, 4176], [4241, 4148], [4198, 4136], [4092, 4098], [3881, 3989], [3761, 3901], [3666, 3811], [3525, 3640], [3403, 3461], [3368, 3406], [3260, 3228], [3209, 3140], [3096, 2951], [3049, 2880], [3016, 2833], [2898, 2680], [2852, 2625], [2796, 2564], [2748, 2524], [2669, 2482]]
    return jsonify(coordinateList)   

def movebackwards():
    pass
  
@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
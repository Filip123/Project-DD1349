from app import app
from flask import render_template


#Home page
@app.route("/")
def index():
    return render_template("mainPage.html")

def moveforwards():
    pass
    

def movebackwards():
    pass
    
   

@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
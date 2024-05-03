from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("mainPage.html")

@app.route('/race-view')
def race_view():
    return render_template('raceview.html')
from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/services")
def services():
    return render_template("public/services.html")

@app.route("/about")
def about():
    return render_template("public/about.html")


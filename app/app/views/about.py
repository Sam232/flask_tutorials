from app import app

@app.route("/about")
def about():
    return "All about Flask!"
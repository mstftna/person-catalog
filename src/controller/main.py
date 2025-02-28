from src import app
from flask import render_template
from flask_login import login_required, current_user

@app.route("/main")
@login_required
def main():
    return render_template("index.html",
        user=current_user)

@app.route("/categories")
@login_required
def categories():
    return render_template("index.html",
        user=current_user)
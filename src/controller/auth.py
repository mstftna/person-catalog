from src import app, login_manager
from flask_login import login_user, login_required, logout_user, current_user
from flask import request, redirect, render_template, url_for, render_template_string
from src.model.User import User


users = {"user": User("user", "1234")}

@login_manager.user_loader
def user_loader(id):
    return users.get(id)

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")
        

@app.route("/auth", methods=['POST'])
def auth():
    user = users.get(request.form["email"])

    if user is None or user.password != request.form["password"]:
        return redirect(url_for("login"))

    login_user(user)
    return redirect(url_for("main"))


# @app.route("/protected")
# @login_required
# def protected():
#     return render_template_string(
#         "Logged in as: {{ user.id }}",
#         user=current_user
#     )

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('logout'))
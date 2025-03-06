from src import app, login_manager
from flask_login import login_user, login_required, logout_user, UserMixin, current_user
from flask import request, redirect, render_template, url_for, render_template_string
from src.model.Auth import Auther, User, users

auther = Auther()



@login_manager.user_loader
def user_loader(uname):
    if uname not in users:
        return

    user = User(uname)
    return user


@login_manager.request_loader
def request_loader(request):
    uname = request.form.get('uname')
    if uname not in users:
        return

    user = User()
    user.id = uname
    return user

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")
        

@app.route("/auth", methods=['POST'])
def auth():
    uname = request.form['uname']
    password = request.form["password"]
    if auther.checkUser(uname, password):
        user = User(uname)
        login_user(user)
        return redirect(url_for('main'))

    return 'Bad login'

@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401
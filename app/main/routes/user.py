from flask import Blueprint, render_template, session, url_for
from ..services.user_services import *
from ..forms.forms import LoginForm, RegisterForm
import json


user = Blueprint('user', __name__)

@user.route('/')
def home():
    return render_template("index.html")


@user.route('/add', methods=['GET','POST'])
def new_user():
    # result = add_user()
    form = RegisterForm()
    if form.validate_on_submit():
        result = add_user(form)
        output = json.loads(result)
        if output["status"] == True:
            message = output["message"]
            category = output["category"]
            flash(message, category)
            return redirect('/')
        else:
            message = output["message"]
            category = output["category"]
            flash(message, category)
    return render_template("register.html", title="Sign Up", form=form)


@user.route('/login', methods=['GET','POST'])
def user_login():
    # result = login()
    if session.get('user_name'):
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        result = login(form)
        output = json.loads(result)
        if output["status"] == True:
            message = output["message"]
            category = output["category"]
            flash(message, category)
            session['user_id'] = output["user_id"]
            session['user_name'] = output["user_name"]
            session['user_type'] = output["user_type"]
            session['user_mobile'] = output["user_mobile"]
            session['user_email'] = output["user_email"]
            return redirect('/')
        else:
            message = output["message"]
            category = output["category"]
            flash(message, category)
    return render_template("login.html", title="Sign In", form=form)

@user.route("/logout", methods=["POST", "GET"])
def user_logout():
    session["user_name"] = False
    session.pop("user_id", None)
    session.pop("user_type", None)
    return redirect('/')

@user.route("/profile", methods=["POST", "GET"])
def user_profile():
    if not session.get('user_name'):
        return redirect(url_for('user.user_login'))
    
    return render_template("profile.html", title="My Account")



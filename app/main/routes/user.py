from flask import Blueprint, render_template
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
    form = LoginForm()
    if form.validate_on_submit():
        result = login(form)
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
    return render_template("login.html", title="Login", form=form)



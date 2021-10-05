from ..models.UserModel import UserModel, db
from sqlalchemy import exc
from flask import request,redirect, flash
import json


def add_user(form):
    try:
        # user_name = request.json['user_name']
        # mobile = request.json['mobile']
        # email = request.json['email']
        # password = request.json['password']
        # role = request.json['role']
        user_name = request.form.get("user_name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        password = request.form.get("password")
        role = "user"
        user_email = UserModel.query.get(email)
        user = UserModel(
            name = user_name,
            mobile = mobile,
            email = email,
            password = password,
            role = role
        )
        db.session.add(user)
        db.session.commit()
        return json.dumps({
            "message": "You are successfully registered!",
            "status": True,
            "category": "success"
        })
    except exc.IntegrityError:
        return json.dumps({
            "message": "Mobile number or email already exists",
            "status": False,
            "category": "danger"
        })
    except exc.SQLAlchemyError as err:
        error = str(err)
        return json.dumps({
            "message": error,
            "status": False,
            "category": "danger"
        })


def login(form):
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        user_email = UserModel.query.filter_by(email=email).first()
        user_pwd = UserModel.query.filter_by(password=password).first()
        if user_email and user_pwd:
            return json.dumps({
                "message": "Login successfully",
                "status": True,
                "category": "success"
            })
        elif user_email and not user_pwd:
            return json.dumps({
                "message": "Password doesn't match",
                "status": False,
                "category": "danger"
            })
        elif not user_email and user_pwd:
            return json.dumps({
                "message": "User name doesn't exist",
                "status": False,
                "category": "danger"
            })
        else:
            return json.dumps({
                "message": "User email or password is incorrect",
                "status": False,
                "category": "danger"
            })
    except exc.SQLAlchemyError as err:
        error = str(err)
        return json.dumps({
            "message": error,
            "status": False,
            "category": "danger"
        })


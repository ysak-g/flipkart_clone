from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    email       =   StringField("Email", validators=[DataRequired()])
    password    =   StringField("Password", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")


class RegisterForm(FlaskForm):
    user_name           =   StringField("Username", validators=[DataRequired()])
    email               =   StringField("Email", validators=[DataRequired(), Email()])
    mobile              =   StringField("Mobile No", validators=[DataRequired()])
    password            =   StringField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    confirm_password    =   StringField("Confirm Password", validators=[DataRequired(), Length(min=6,max=15), EqualTo('password')])
    submit              =   SubmitField("Sign Up")

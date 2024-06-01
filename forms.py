from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)]) #Creates a text field for the username
    password = PasswordField('Password', validators=[DataRequired()]) #Creates a password field for the password
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) #Creates a password field for the password confirmation
    submit = SubmitField('Sign Up') #Creates a submit button

    def validate(self, username):
        user = User.query.filter_by(username=username.data).first() #Queries the database for the user
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")
        

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) #Creates a text field for the username 
    password = PasswordField('Password', validators=[DataRequired()]) #Creates a password field for the password
    remember = BooleanField('Remember Me') #Creates a checkbox for the remember me option
    submit = SubmitField('Login') #Creates a submit button
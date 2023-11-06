# Importing the class FlaskForm from the flask_wtf module, remembering that module is a group of different classes and functions
from flask_wtf import FlaskForm
# The fields basically represent the type of the input, like in html, "<input type='text'>" for example. >
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired

# To create a form using the Flask_wtf module we use classes
class RegistrationForm(FlaskForm): # The name of the class will be the name of the form
    # The first parameter passed to the class is the label's name
    # Secondly you can add the validators
    username = StringField('Username', validators=[Length(min=5, max=20), DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
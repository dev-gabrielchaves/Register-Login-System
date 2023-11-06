from flask import render_template, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Note that you don’t have to pass request.form to Flask-WTF, it will load automatically. And the convenient validate_on_submit will check if it is a POST request and if it is valid.
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Instantiating class User and giving it's attribute 
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Adding user to the database
        db.session.add(user)
        db.session.commit()
        # The flashing system basically makes it possible to record a message at the end of a request and access it next request and only next request.
        # Another thing about flash messages, you got have a secret key set, otherwise it won't work
        flash("You've been registered successfully!") # So here I've set a flash message, and that message will just be used for the next request
        return redirect(url_for('login'))
    # print(form.errors) -> Just for testing, in case of a wrong password it will show: {'confirm_password': ['Field must be equal to password.']}
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You've been logged in successfully!")
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
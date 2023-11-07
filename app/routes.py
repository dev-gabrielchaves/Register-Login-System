from flask import render_template, redirect, url_for, flash, session, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/')
def home():
    return render_template('home.html', username=session.get('username'))

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
        session['id'] = user.id
        session['username'] = user.username
        session['email'] = user.email
        return redirect(url_for('home'))
    # print(form.errors) -> Just for testing, in case of a wrong password it will show: {'confirm_password': ['Field must be equal to password.']}
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("You've been logged in successfully!")
            session['id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            return redirect(url_for('home'))
        else:
            flash("Couldn't find the user. Please check your email and password.")
    return render_template('login.html', form=form)

# Clears the session
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# You just be allowed to access this page in case there is some user in the session
@app.route('/protected')
def protected():
    if session.get('username'): 
        return render_template('protected.html', id=session.get('id'), 
                               username=session.get('username'), 
                               email=session.get('email'))
    else:
        return(redirect(url_for('login')))
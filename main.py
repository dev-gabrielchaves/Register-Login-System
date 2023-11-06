from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This Is The Secret Key'
# Setting the URI where our database will be located
# In the case of using a sqlite database, the structure is like the following
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app) # Creating an object db, instace of the class SQLAlchemy, that will allow us to work with the database
app.app_context().push()

# SQLAlchemy allow us to work with classes when setting our tables to the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Note that you don’t have to pass request.form to Flask-WTF, it will load automatically. And the convenient validate_on_submit will check if it is a POST request and if it is valid.
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

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This Is The Secret Key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Note that you don’t have to pass request.form to Flask-WTF, it will load automatically. And the convenient validate_on_submit will check if it is a POST request and if it is valid.
        # The flashing system basically makes it possible to record a message at the end of a request and access it next request and only next request.
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
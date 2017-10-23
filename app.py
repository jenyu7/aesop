import sqlite3
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

# hard coded user info for now
USERS = ['bob', 'elmo']
PASSWORDS = ['bobbins', 'goldfish']

@app.route('/')
def root():
    return render_template("base.html")

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    # if logged in redirect to landing page
    if session.get('username'):
        return redirect(url_for('profile'))
    # if user did not enter the form display the form
    if not request.form.get('username'):
        return render_template('login.html')
    # else authenticate
    if request.form.get('username') in USERS:
        if request.form.get('password') == PASSWORDS[USERS.index(request.form.get('username'))]:
            session['username'] = request.form.get('username')
            return redirect(url_for('profile'))
        else:
            flash("Bad password")
            return redirect(url_for('auth'))
        return "foo"
    else:
        flash("Bad username")
        return redirect(url_for('auth'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if session.get('username'):
        return redirect(url_for('profile'))
    return render_template('signup.html')



@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('username'):
        flash("Not logged in")
        return redirect(url_for('root'))
    return render_template('profile.html', user=session.get('username'))


if __name__ == "__main__":
    app.debug = True
    app.run()

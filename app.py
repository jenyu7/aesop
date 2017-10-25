import sqlite3
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from utils import auth

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def root():
    return render_template("base.html")


@app.route('/auth', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to profile
    if session.get('username'):
        return redirect(url_for('profile'))
    # user entered login form
    elif request.form.get('login'):
        return auth.login()
    # user entered signup form
    elif request.form.get('signup'):
        return auth.signup()
    # user didn't enter form
    else:
        return render_template('auth.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('username'):
        flash("Not logged in")
        return redirect(url_for('auth'))
    return render_template('profile.html', user=session.get('username'))


if __name__ == "__main__":
    app.debug = True
    app.run()

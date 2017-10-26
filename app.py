import sqlite3
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from utils import auth, edit

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
        return redirect(url_for('authentication'))
    return render_template('profile.html', user=session.get('username'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if not session.get('username'):
        flash("Not logged in")
    else:
        flash("Logged out")
        session.pop('username')
    return redirect(url_for('authentication'))


@app.route('/add_story', methods=['GET', 'POST'])
def add_story():
    if not session.get('username'):
        flash("You must log in to add on to the story!")
        return redirect(url_for('authentication'))
    elif request.form.get("update"):
        content = request.form.get("content")
        return edit.add(content)
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.debug = True
    app.run()

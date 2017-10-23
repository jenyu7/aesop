import sqlite3
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def root():
    return render_template("base.html")

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if session.get('username'):
        return redirect(url_for('profile'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if session.get('username'):
        return redirect(url_for('profile'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('username'):
        flash("Not logged in")
        return redirect(url_for('root'))


if __name__ == "__main__":
    app.debug = True
    app.run()

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

def login():
    '''
    Logs user in.
    '''
    if request.form.get('username') in USERS:
        if request.form.get('password') == PASSWORDS[USERS.index(request.form.get('username'))]:
            session['username'] = request.form.get('username')
            return redirect(url_for('profile'))
        else:
            flash("Bad password")
            return redirect(url_for('auth'))
    else:
        flash("Bad username")
        return redirect(url_for('auth'))

def signup():
    '''
    Signs user up for the website.
    CANNOT BE DONE UNTIL DATABASES ARE DONE
    '''
    return "CANNOT BE DONE UNTIL DATABASES ARE DONE<br>HARD CODED USERNAME AND PASSWORD IS 'elmo' and 'goldfish'"

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    # if user already logged in, redirect to profile
    if session.get('username'):
        return redirect(url_for('profile'))
    # user entered login form
    elif request.form.get('login'):
        return login()
    # user entered signup form
    elif request.form.get('signup'):
        return signup()
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

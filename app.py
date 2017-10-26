import sqlite3
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from utils import auth, edit

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Login Authentication
@app.route('/auth', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        return redirect(url_for('base'))
    # user entered login form
    elif request.form.get('login'):
        return auth.login()
    # user entered signup form
    elif request.form.get('signup'):
        return auth.signup()
    # user didn't enter form
    else:
        return render_template('auth.html')

# Homepage after user has logged in - *shows list of stories they can edit
@app.route('/')
def root():
    return redirect('base')

@app.route('/base')
def homepage():
    return render_template('base.html')

# Profile page - shows profile stats and (if time, allow them to change password)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('username'):
        flash("Not logged in")
        return redirect(url_for('authentication'))
    return render_template('profile.html', user=session.get('username'))

# Logged Out Page
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if not session.get('username'):
        flash("Not logged in")
    else:
        flash("Logged out")
        session.pop('username')
    return redirect(url_for('authentication'))

# Add to an existing story
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

# Create a new story
@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if not session.get('username'):
        flash("You must log in to create a story!")
        return redirect(url_for('authentication'))
    elif request.form.get("create"):
        title = request.form.get("title")
        content = request.form.get("content")
        return edit.create(title,content)
    return render_template("create_story.html")

# Show the stories you've edited
@app.route ('/editedStories')
def edited_stories():
    if not session.get('username'):
        flash("You must log in to view your stories!")
        return redirect(url_for('authentication'));
    else:
        return render_template('add.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

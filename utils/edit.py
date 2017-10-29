from flask import Flask, render_template, redirect, url_for, request, session, flash
import database

def create(title, content):
    # sID = database.new_sID()
    # database.create(sID, title, "\n" + content)
    flash("added " + str(title) + ": " + str(content))
    return redirect(url_for('profile'))

def add(user, content):
    database.addUpdate(0, str(user), str(content))
    flash("added " + str(content) + "!!")
    return redirect(url_for('profile'))

# creates story id from max_id + 1
def create_id():
    pass

#checks if user has already edited story
def verify(id):
    user = session.get('username')
    history =  database.getHistory(id)
    try:
        if history.index(user) >= 0:
            return False
    except:
        return True

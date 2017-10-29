from flask import Flask, render_template, redirect, url_for, request, session, flash
import database

def login():
    '''
    Logs user in.
    '''
    users = database.getUsers()
    print users
    if request.form.get('username') in users:
        if request.form.get('password') == users[request.form.get('username')]:
            session['username'] = request.form.get('username')
            return redirect(url_for('profile'))
        else:
            flash("Bad password")
            return redirect(url_for('authentication'))
    else:
        flash("Bad username")
        return redirect(url_for('authentication'))

def signup():
    '''
    Signs user up for the website.
    '''
    users = database.getUsers()
    # if username already taken, redirect to auth page
    if request.form.get('username') in users:
        flash("Username already taken")
    elif request.form.get('password0') != request.form.get('password1'):
        flash("Passwords do not match")
    else:
        flash("Please log in with your new credentials!")
        database.addUser(request.form.get('username'), request.form.get('password0'))
    return redirect(url_for('authentication'))

if __name__ == '__main__':
    database.addUser("elmo", "goldfish")
    print database.getUsers()

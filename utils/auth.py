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
    return "CANNOT BE DONE UNTIL DATABASES ARE DONE<br>HARD CODED USERNAME AND PASSWORD IS 'elmo' and 'goldfish'"

if __name__ == '__main__':
    database.addUser("elmo", "goldfish")
    print database.getUsers()

from flask import Flask, render_template, redirect, url_for, request, session, flash

# hard coded user info for now
USERS = ['bob', 'elmo']
PASSWORDS = ['bobbins', 'goldfish']

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
            return redirect(url_for('authentication'))
    else:
        flash("Bad username")
        return redirect(url_for('authentication'))

def signup():
    '''
    Signs user up for the website.
    CANNOT BE DONE UNTIL DATABASES ARE DONE
    '''
    return "CANNOT BE DONE UNTIL DATABASES ARE DONE<br>HARD CODED USERNAME AND PASSWORD IS 'elmo' and 'goldfish'"

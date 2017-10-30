from flask import redirect, url_for, request, session, flash
import database

# scrits for logging in


# Logs user in (from form)
def login():
    users = database.getUsers()
    # checks credentials for login
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


# Signs user up for the website (from form)
def signup():
    users = database.getUsers()
    # checks if credentials for flash message
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

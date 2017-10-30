from flask import redirect, session, flash
import database

# scripts for editing stories


def create(user, title, content):
    sID = database.new_sID()
    database.create(sID, title, content, user)
    flash("added " + str(title) + ": " + str(content))
    return redirect('edited_stories')


def add(sID, user, content):
    database.addUpdate(sID, str(user), str(content))
    flash("added " + str(content) + "!!")
    return redirect('base')


# checks if user has already edited story
def verify(id):
    user = session.get('username')
    history = database.getHistory(id)
    try:
        if history.index(user) >= 0:
            print "contributed"
            return False
    except:
        print "nada"
        return True

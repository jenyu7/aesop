import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from utils import auth, edit, database


app = Flask(__name__)
app.secret_key = os.urandom(32)


# Login Authentication
@app.route('/login', methods=['GET', 'POST'])
def authentication():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        return redirect('base')
    # user entered login form
    elif request.form.get('login'):
        print "login"
        return auth.login()
    # user didn't enter form
    else:
        return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def crt_acct():
    if session.get('username'):
        return redirect('base')
     # user entered signup form
    elif request.form.get('signup'):
        return auth.signup()
    else:
        return render_template('signup.html')


# Homepage after user has logged in - *shows list of stories they can edit
@app.route('/')
def root():
    if not("elmo" in database.getUsers()):
        database.addUser("elmo","goldfish")
    return redirect('base')


@app.route('/base')
def homepage():
    # print database.getStory(0)
    # Dictionary for stories in the form of Title: [id, content]
    stories = {}
    L = [-1, ""]
    # While there is still another story in the story database, display it
    story_id = 0
    while story_id >= 0:
        try:
            info = database.getStory(story_id)
            stories[info[1]] = [story_id, info[3]]
            story_id += 1
        except:
            print "No more stories in database."
            break;
    print stories
    return render_template('base.html', stories=stories)


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
'''
@app.route('/view_story')
def view():
    if request.args.get('sID')
'''

# Add to an existing story
@app.route('/add_story', methods=['GET', 'POST'])
def add_story():
    if not session.get('username'):
        flash("You must log in to add on to the story!")
        return redirect(url_for('authentication'))
    elif request.form.get("update"):
        user = session.get('username')
        content = request.form.get("content")
        return edit.add(user, content)
    else:
        id = request.args.get("id")
        print "-------------\n\n"
        print id
        print "-------------\n\n"
        if edit.verify(id):
            print "render add"
            return render_template("add.html")
        else:
            flash("You have already contributed to this story.")
            return redirect(url_for('profile'))

# Create new story
@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if not session.get('username'):
        flash("You must log in to create a new story!")
        return redirect(url_for('authentication'))
    elif request.form.get("create"):
        title = request.form.get("title")
        content = request.form.get("content")
        return edit.create(title, content)
    else:
        return render_template("create.html")


# Show the stories you've edited
@app.route('/edited_stories')
def edited_stories():
    if not session.get('username'):
        flash("You must log in to view your stories!")
        return redirect(url_for('authentication'))
    else:
        ids = database.getUserStories("jen")
        print ids
        # Dictionary for stories in the form of Title: id
        stories = {}
        # While there is still another story in the story database, display it
        i = 0
        while i < len(ids):
                info = database.getStory(ids[i])
                print "info: ", info
                stories[info[1]] = ids[i]
                i += 1
        print stories
        return render_template('edited_stories.html', stories=stories)

# View each edited story in full
@app.route('/view_story')
def view_story():
    if not session.get('username'):
        flash("You must log in to view your stories!")
        return redirect(url_for('authentication'))
    else:
        return "Popcorn"

if __name__ == "__main__":
    app.debug = True
    app.run()

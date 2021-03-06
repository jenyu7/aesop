import sqlite3

# requested functions:


# execute this file to create the initial database
if __name__ == '__main__':
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    # table for user login
    c.execute("CREATE TABLE users (user TEXT, pass TEXT, PRIMARY KEY(user))")
    # table for story ID storage; id is text because it's user created
    c.execute("CREATE TABLE stories (sID TEXT, name TEXT, full TEXT, last TEXT, PRIMARY KEY(sID))")
    # table for update history for all stories
    c.execute("CREATE TABLE history (sID TEXT, user TEXT, entry TEXT, PRIMARY KEY(sID, user))")
    # hard coded starting story
    c.execute("INSERT INTO stories VALUES(0, 'jen', 'hello there', 'there')")
    # save and close database
    db.commit()
    db.close()


# -----FUNCTIONS FOR LOGIN SYSTEM-----


# returns a dictionary for user data {user: pass}
def getUsers():
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT user, pass FROM users'
    x = c.execute(a)
    users = {}
    for line in x:
        users[line[0]] = line[1]
    db.close()
    return users


# add the login to the database
def addUser(user, password):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    vals = [user, password]
    c.execute("INSERT INTO users VALUES(?, ?)", vals)
    db.commit()
    db.close()

# --------------------------------------------------

# -----FUNCTIONS FOR STORY CREATE/ADDTIONS/ACCESSORS-----

# ---STORY CREATION---


# generates a new id for the story (sID)
# returns the next available sID
def new_sID():
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    data = c.execute("SELECT MAX(sID) FROM stories")
    print data
    try:
        for i in data:
            max_id = i[0]
        return int(max_id) + 1
    except:
        return 0


# adds a row to stories with these starting values
def create(sID, title, content, user):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    vals0 = [str(sID), title, content, content]
    vals1 = [str(sID), user, content]
    c.execute("INSERT INTO stories VALUES(?, ?, ?, ?)", vals0)
    c.execute("INSERT INTO history VALUES(?, ?, ?)", vals1)
    db.commit()
    db.close()


# adds the update to database (history and stories)
def addUpdate(sID, user, entry):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    # add the entry into history
    vals0 = [str(sID), user, entry]
    c.execute("INSERT INTO history VALUES (?,?,?)", vals0)
    # update the story
    story = getStory(sID)
    story[2] = story[2] + " " + entry
    story[3] = entry
    vals1 = [story[2], story[3], story[0]]
    c.execute("UPDATE stories SET full = ?, last = ? WHERE sID = ?", vals1)
    db.commit()
    db.close()


# returns a list for said story [story id, name of story, full story, last update]
def getStory(sID):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT sID, name, full, last FROM stories WHERE sID = ' + str(sID)
    x = c.execute(a)
    v = x.fetchone()
    return [v[0], v[1], v[2], v[3]]


# returns users which have edited a certain story
def getHistory(story_id):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    x = c.execute('SELECT user FROM history WHERE sID = ?', [story_id])
    users = []
    for line in x:
        users.append(line[0])
    db.close()
    return users


# Given a username, return a list of all the story ids that the user has edited
# SELECT sID from history WHERE user = <username>
def getUserStories(username):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT sID FROM history WHERE user="' + username + '"'
    print "a: " + a
    x = c.execute(a)
    stories = []
    for line in x:
        stories.append(line[0])
    db.close()
    return stories

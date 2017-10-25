import sqlite3

# requested functions:
#


# execute this file to create the initial database
if __name__ == '__main__':
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    # table for user login
    c.execute("CREATE TABLE users (user TEXT, pass TEXT, PRIMARY KEY(user))")
    # table for story ID storage; id is text because it's user created
    c.execute("CREATE TABLE stories (sID TEXT, name TEXT, PRIMARY KEY(sID))")
    # table for update history for all stories
    c.execute("CREATE TABLE history (sID TEXT, user TEXT, entry TEXT, PRIMARY KEY(sID, user))")
    # save and close database
    db.commit()
    db.close()

# tracks if the seperate story databases need
# initialized as false since you can only change the data with this module
story_update = False


# returns a dictionary for user data {user: pass}
def getUsers():
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT user, pass FROM users'
    x = c.execute(a)
    users = {}
    for line in x:
        users[line[0]] = line[1]
    db.close()
    return users


# returns a dictionary for story names {sID: name}
def getStories():
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT sID, name FROM stories'
    x = c.execute(a)
    stories = {}
    # sID is stored as TEXT so delete int cast if it happens to be an issue
    #   also add in a str cast around sID in getStory() and update despcription
    for line in x:
        stories[int(line[0])] = line[1]
    db.close()
    return stories


# returns a list of lists (in order) for story entries [[user, entry],...]
def getStory(sID):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    name = getStories()[sID]
    a = 'SELECT user, entry FROM ' + name
    x = c.execute(a)
    story = []
    for line in x:
        story.append([line[0], line[1]])
    db.close()
    return story


# returns a list of lists for all story histories [[sID, user, entry],...]
# not sure how else to return rows of 3 values
def getHistory():
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT sID, user, entry FROM history'
    x = c.execute(a)
    history = []
    for line in x:
        history.append([line[0], line[1], line[2]])
    db.close()
    return history


# helper to insert a list of values into the table
def insert(table, vals):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    x = "INSERT INTO " + table + " VALUES ("
    # add in the values into command
    for a in vals:
        x += "'" + a + "', "
    # get rid of last comma
    x = x[:len(x) - 2]
    db.close()
    return x + ")"


# create a table for that story
def create(story):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    c.execute("CREATE TABLE " + story + " (user TEXT, entry TEXT, PRIMARY KEY (user))")
    db.commit()
    db.close()


# add the loggin to the database
def addUser(user, password):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    vals = [user, password]
    c.execute(insert("users", vals))
    db.commit()
    db.close()


# creates and adds the story to the database
def addStory(sID, story):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    create(story)
    vals = [str(sID), story]
    c.execute(insert("stories", vals))
    db.commit()
    db.close()


def addUpdate(sID, user, entry):
    # initialize database
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    vals = [str(sID), user, entry]
    c.execute(insert("history", vals))
    story = getUsers()[str(sID)]
    vals.pop(str(sID))
    c.execute(insert(story, vals))
    db.commit()
    db.close()

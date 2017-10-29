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
    # save and close database
    db.commit()
    db.close()

#-----HELPER FUNCTIONS-----

# helper to make insert statement
def insert(table, vals):
    x = "INSERT INTO " + table + " VALUES ("
    # add in the values into command
    for a in vals:
        x += "'" + a + "', "
    # get rid of last comma
    x = x[:len(x) - 2]
    return x + ")"

#---------------------------

    
#-----FUNCTIONS FOR LOGIN SYSTEM-----
    
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
    c.execute(insert("users", vals))
    db.commit()
    db.close()

#------------------------------------

#-----FUNCTIONS FOR STORY CREATE/ADD-----

#---STORY CREATION---

# generates a new id for the story (sID)
def new_sID():
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    max_id = c.execute("SELECT MAX(sID) FROM stories")
    print max_id
    # return int(max_id[0][0]) + 1

# adds a row to stories with these starting values
def create(sID, name, update):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    vals = [str(sID), name, update, update]
    c.execute(insert("stories", vals))
    db.commit()
    db.close()

# helper to make update statement for story
def update(vals):
    x = "UPDATE stories SET full = '" + vals[2] + "' && last = '" + vals[3] + "' "
    x += "WHERE sID = '" + str(vals[0]) + "'"
    return x

# adds the update to database (history and stories)
def addUpdate(sID, user, entry):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    # add the entry into history
    vals = [str(sID), user, entry]
    c.execute(insert("history", vals))
    # update the story
    story = getStory(sID)
    story[2].append(entry)
    story[3] = entry
    c.execute(update(story))
    db.commit()
    db.close()

#---------------------------------------

# returns a list for said story [name of story, full story, last update]
def getStory(sID):
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT name, full, last FROM stories WHERE sID = ' + str(sID)
    x = c.execute(a)
    #x = x[0]
    print "________________________\n\n"
    print x.fetchall()[0]
    print"\n\n________________________________\n\n"
    v = x.fetchall()[0]
    return [v[0], v[1], v[2]]


# returns a list of lists for all story histories [[sID, user, entry],...]
# not sure how else to return rows of 3 values
def getHistory():
    db = sqlite3.connect("data/aesop.db")
    c = db.cursor()
    a = 'SELECT sID, user, entry FROM history'
    x = c.execute(a)
    history = []
    for line in x:
        history.append([line[0], line[1], line[2]])
    db.close()
    return history


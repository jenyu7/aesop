import csv, sqlite3

# initialize database
db = sqlite3.connect("aesop.db")
c = db.cursor()

# execute this file to create the initial database
if __name__ == '__main__':
    # table for user login
    c.execute("CREATE TABLE users (user TEXT, pass TEXT, PRIMARY KEY(user))" )
    # table for story ID storage; id is text because it's user created
    c.execute("CREATE TABLE stories (sID TEXT, name TEXT, PRIMARY KEY(sID))")
    # table for update history for all stories; process this into the stories page
    c.execute("CREATE TABLE history (sID TEXT, user TEXT, entry TEXT, PRIMARY KEY(sID, user))")
    # save and close database
    db.commit()
    db.close()

# returns a dictionary for user data {user: pass}
def getUsers():
    foo = 'SELECT user, pass FROM users WHERE peeps.id = courses.id'
    x = c.execute(foo)
    users = {}
    for line in x:
        users[line[0]] = line[1]
    return users

# helper to insert a list of values into the table
def insert(table, vals):
    x = "INSERT INTO " + table + " VALUES ("
    # add in the values into command
    for a in vals:
        x += "'" + a + "', "
    # get rid of last comma
    x = x[:len(x) - 2]
    return x + ")"


# a table for that story
def create(story):
    c.execute("CREATE TABLE " + story + " (user TEXT, update TEXT, PRIMARY KEY (user))")
    db.commit()

# add the loggin to the database
def addUser(nick, user, password):
    vals = [nick, user, password]
    c.execute(insert("users", vals))


def addStory(sID, Story):
    pass

def addUpdate(sID, user, entry):
    pass

def getStories():
    pass

def updateStories():
    pass

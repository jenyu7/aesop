import csv, sqlite3

# initialize database
db = sqlite3.connect("aesop.db")
c = db.cursor()

# execute this file to create the initial database
if __name__ == '__main__':
    # table for user login
    c.execute("CREATE TABLE users (nick TEXT, user TEXT, pass TEXT, PRIMARY KEY(user))" )
    # table for story ID storage; id is text because it's user created
    c.execute("CREATE TABLE stories (sID TEXT, name TEXT, PRIMARY KEY(user))")
    # table for update history for all stories; process this into the stories page
    c.execute("CREATE TABLE history (sID TEXT, user TEXT, add TEXT, PRIMARY KEY(sID, user))")
    # save and close database
    db.commit()
    db.close()

# a table for that story
def create(name):
    c.execute("CREATE TABLE " + name + " (user TEXT, update TEXT, PRIMARY KEY (user))")
    db.commit()

# add the loggin to the database
def addUser(nick, user, pass):
    c.execute("INSERT INTO users VALUES ('" + nick + "', '" + user + "', '" + pass + "')"")

# Team aesop

## Roster

Arif Roktim, Charles Weng, Jenny Yu, Shannon Lau, Samantha Ngo

### Collaborative Story Telling Website

We are making a website where users can collaboratively create stories. However, the users can only view the most recently added addition when adding to the story. They can only view the whole story after adding to the story.

### Dependencies

* Flask
* Python

In order to run the application you need to install flask. Preferably you should install this in a virtual environment so that it doesn't mess with your root python install. Please run the following commands:

```
$ pip install virtualenv
$ virtualenv <name>
$ . <name>/bin/activate
or for windows
$ . <name>/script/activate
```

You can then install flask by:
`$ pip install flask`

### Running the application:

To clone the repo run

`$ git clone https://github.com/jenyu7/aesop.git`

After doing so, you can run the application by cding into the repo and running:

```
$ cd aesop
$ python utils/database.py
$ python app.py
```

You can then view the webpage by opening the url `localhost:5000` in a web browser.

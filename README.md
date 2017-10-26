# aesop

To clone the repo run

`$ git clone https://github.com/jenyu7/aesop.git`

In order to run the application you need to install flask. Preferably you should install this in a virtual environment so that it doesn't mess with your root python install

```
$ pip install virtualenv
$ virtualenv <name>
$ . <name>/bin/activate
or for windows
$ . <name>/script/activate
```

You can then install flask by:
`$ pip install flask`

After doing so, you can run the application by cding into the repo and running:

```
$ cd aesop
$ python utils/database.py
$ python app.py
```

You can then view the webpage by opening the url `localhost:5000` in a web browser.

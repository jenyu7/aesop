from flask import Flask, render_template, redirect, url_for, request, session, flash
import database

def create(title, content):
    database.create(
    flash("added " + str(title) + ": " + str(content))
    return redirect(url_for('profile'))

def add(content):
    flash("added " + str(content) + "!!")
    return redirect(url_for('profile'))

# creates story id from max_id + 1
def create_id():
    pass

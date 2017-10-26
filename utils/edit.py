from flask import Flask, render_template, redirect, url_for, request, session, flash
import database

def create():
    return 0;

def add(content):
    flash("added " + str(content) + "!!")
    return redirect(url_for('profile'))



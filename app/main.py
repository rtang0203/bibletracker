from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

readToday = False

@main.route('/', methods = ('GET', 'POST'))
def index():
    if request.method == 'POST':
        global readToday
        readToday = True
    #return render_template('index.html', messages = messages)
    return render_template('index.html', readToday = readToday)

@main.route('/reset', methods = ['POST'])
def reset():
    if request.method == 'POST':
        global readToday
        readToday = False
    return redirect(url_for('main.index'))
    #return render_template('index.html', readToday = readToday)

@main.route('/profile')
def profile():
    return render_template('profile.html')
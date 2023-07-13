from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from .models import ReadingLog
from datetime import date
from . import db

main = Blueprint('main', __name__)

def hasReadToday():
    if current_user.is_authenticated:
        todaysEntry = ReadingLog.query.filter_by(user_id=current_user.id, date=date.today()).first()
        if todaysEntry:
            return True
    return False

@main.route('/', methods = ['GET'])
def index():
    if current_user.is_authenticated:
        return render_template('index.html', readToday = hasReadToday(), name=current_user.name)
    return render_template('index.html', readToday = False)

@main.route('/', methods = ['POST'])
@login_required
def index_post():
    userId = current_user.id 
    currentDate = date.today()

    # Create a new ReadingLog entry
    entry = ReadingLog(user_id=userId, date=currentDate)

    # Add the entry to the database
    db.session.add(entry)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/reset', methods = ['POST'])
@login_required
def reset():
    if request.method == 'POST':
        # global readToday
        # readToday = False
        if current_user.is_authenticated:
            todaysEntry = ReadingLog.query.filter_by(user_id=current_user.id, date=date.today()).first()
            if todaysEntry:
                db.session.delete(todaysEntry)
                db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/profile')
@login_required
def profile():
    pastEntries = []
    if current_user.is_authenticated:
        pastEntries = ReadingLog.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', name=current_user.name, entries=pastEntries)
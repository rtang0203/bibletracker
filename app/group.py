from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from .models import ReadingLog, Group, GroupMember
from datetime import date
from . import db

group = Blueprint('group', __name__)

@group.route('/groups')
@login_required
def showGroups():
    groupNames = []
    if current_user.is_authenticated:
        yourGroups = Group.query.join(GroupMember).filter(GroupMember.user_id == current_user.user_id).all()
        groupNames = [g.group_name for g in yourGroups]
    return render_template('profile.html', name=current_user.name, groupNames=groupNames)

#create group. adds just you at the start
def createGroup():
    pass

#single group. from here you can add members as well as see todays readings for your group members
def showGroup():
    pass

#add member to group. should only be reachable from a form in the showSingleGroup page
def addMember():
    pass


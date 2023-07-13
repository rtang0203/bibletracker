from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from .models import ReadingLog, ReadingGroup, GroupMember
from datetime import date
from . import db

group = Blueprint('group', __name__)

@group.route('/groups')
@login_required
def showGroups():
    groupNames = []
    if current_user.is_authenticated:
        yourGroups = ReadingGroup.query.join(GroupMember, GroupMember.group_id == ReadingGroup.id).filter(GroupMember.user_id == current_user.id).all()
        groupNames = [g.group_name for g in yourGroups]
    return render_template('groups.html', name=current_user.name, yourGroups=yourGroups)

#create group. adds just you at the start
@group.route('/newgroup', methods=['POST'])
def createGroup():
    groupName = request.form.get('groupname')
    # group names must be unique
    existingGroup = ReadingGroup.query.filter_by(group_name=groupName).first() 
    if existingGroup:
        flash('Group name already exists')
        return redirect(url_for('group.showGroups'))
    
    new_group = ReadingGroup(group_name=groupName)
    db.session.add(new_group)
    db.session.commit()
    new_group_member = GroupMember(group_id=new_group.id, user_id=current_user.id)
    db.session.add(new_group_member)
    db.session.commit()
    return redirect(url_for('group.show_group', group_id=new_group.id))

#single group. from here you can add members as well as see todays readings for your group members
@group.route('/group/<int:group_id>')
@login_required
def show_group(group_id):
    group = ReadingGroup.query.get_or_404(group_id)
    return render_template('singlegroup.html', group=group)

#add member to group. should only be reachable from a form in the showSingleGroup page
def addMember():
    pass


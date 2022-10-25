from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from .models import Note
from . import db

import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        notes = request.form.listvalues()
        for note in notes:
            for i in range(len(note)):
                new_note = Note(data_of_note=note[i], user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
    return render_template('home.html', user=current_user)


@views.route('/notes')
@login_required
def notes():
    return render_template('notes.html', user=current_user)

from reservierung_svgrafenhausen.models import Event, User
from flask import Blueprint, render_template, flash, jsonify, request
from flask_login import current_user, login_required
from .getSeatNumber import get_seat_number, decrement_seat_number
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/get-seat', methods=['POST'])
def getSeatId():
    s = get_seat_number()
    return jsonify(seat_number=s)


@views.route('/submit-tickets', methods=['POST'])
@login_required
def submitTickets():
    data = json.loads(request.data)
    ticket_count = data['ticket-count']

    # To be completley sure that no one will change this number
    if ticket_count < 1 or ticket_count > 10:
        flash("Irgendwas ist schief gelaufen, bitte versuchen Sie es erneut", category='error')
        return jsonify(False)

    
    for _ in range(ticket_count):
        new_event = Event(confirmed=False, user_id=current_user.id)
        db.session.add(new_event)

    db.session.commit()
    flash(f"Ihnen wurden {ticket_count} Tickets vorgemerkt!", category='success')
    print("Fertig")

    all_events = Event.query.all()

    for event in all_events:
        user = User.query.get(event.user_id)
        print(f"{event} {user.first_name}")

    decrement_seat_number(ticket_count)


    return jsonify(ticket_count)



@views.route('/reservierung', methods=['GET', 'POST'])
@login_required
def reservierung():
    return render_template("reservierung.html", user=current_user)



@views.route('/confirm-ticket', methods=['POST'])
@login_required
def confirmTicket():
    if current_user.admin:
        data = json.loads(request.data)
        if 'ticket-id' in data:
            ticket_id = data['ticket-id']
            event = Event.query.get(ticket_id)
            event.confirmed = True
            db.session.commit()


@views.route('/delete-ticket', methods=['POST'])
@login_required
def deleteTicket():
    if current_user.admin:
        data = json.loads(request.data)
        if 'ticket-id' in data:
            ticket_id = data['ticket-id']
            event = Event.query.filter_by(id=ticket_id)
            event.delete()
            db.session.commit()

            decrement_seat_number(-1)


@views.route('/undo-ticket', methods=['POST'])
@login_required
def undoTicket():
    if current_user.admin:
        data = json.loads(request.data)
        if 'ticket-id' in data:
            ticket_id = data['ticket-id']
            event = Event.query.get(ticket_id)
            event.confirmed = False
            db.session.commit()

            decrement_seat_number(-1)

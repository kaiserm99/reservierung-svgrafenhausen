from .models import Event, User
from .useful_functions import send_email
from flask import Blueprint, render_template, flash, jsonify, request
from flask_login import current_user, login_required
from .getSeatNumber import get_seat_number, decrement_seat_number
from . import db
import json

views = Blueprint('views', __name__)

PRICE = 14


@views.route('/get-seat', methods=['POST'])
def getSeatId():
    s = get_seat_number()
    return jsonify(seat_number=s)


@views.route('/submit-tickets', methods=['POST'])
@login_required
def submitTickets():
    data = json.loads(request.data)
    ticket_count = data['ticket-count']

    seat_number = int(get_seat_number())

    if ticket_count > seat_number:
        flash(f"Es sind leider nur noch {seat_number} Sitzplätze verfügbar. Passen Sie ihre Anzahl an!", category='error')
        return jsonify( status=False )

    # To be completley sure that no one will change this number
    if ticket_count < 1 or ticket_count > 10:
        flash("Der gewünschte Wert ist nicht zwischen einem (1) und zehn (10) Tickets oder keine Zahl!", category='error')
        return jsonify( status=False )

    user = User.query.get(current_user.id)

    if len(user.events) + ticket_count > 10:
        flash("Sie haben schon die maximale Anzahl an Tickets gebucht. Wenden Sie sich an Felix Gatti (felix.gatti@web.de), um evtl. mehr Tickets zu buchen!", category='error')
        return jsonify( status=False )

    # If there are no bookings at all, save it
    user.more_bookings = ( len(user.events) > 0 )
        
    
    for _ in range(ticket_count):
        new_event = Event(confirmed=False, user_id=current_user.id)
        db.session.add(new_event)

    db.session.commit()

    if ticket_count == 1:
        flash(f"Ihnen wurde 1 Ticket vorgemerkt!", category='success')
    else:
        flash(f"Ihnen wurden {ticket_count} Tickets vorgemerkt!", category='success')

    decrement_seat_number(ticket_count)

    return jsonify( status=True)



@views.route('/reservierung', methods=['GET', 'POST'])
@login_required
def reservierung():
    user = User.query.get(current_user.id)
    
    ticket_count = 0
    for event in user.events:
        if not event.confirmed:
            ticket_count += 1

    print(user.more_bookings)

    return render_template("reservierung.html", user=current_user, ticket_count=ticket_count, ticket_price=ticket_count * PRICE, more_bookings=user.more_bookings)


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

            return jsonify()

    return False


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

            # Reset the more_bookings value if the user has no bookings
            user = User.query.get(current_user.id)

            if len(user.events) == 0:
                user.more_bookings = False


            return jsonify()

    return False


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

            # Reset the more_bookings value if the user has no bookings
            user = User.query.get(current_user.id)

            if len(user.events) == 0:
                user.more_bookings = False

            return jsonify()

    return False


@views.route('/send-email', methods=['POST'])
@login_required
def sendEmail():
    if current_user.admin:
        data = json.loads(request.data)
        if 'user-id' in data:
            user_id = data["user-id"]
            user = User.query.get(user_id)

            try:
                send_email(user)
                flash("E-Mail wurde erfolgreich gesendet", category='success')

            except:
                flash("ACHTUNG! E-Mail konnte nicht gesendet werden!", category='error')
            

            return jsonify()
    
    return False


@views.route('/add-ticket', methods=['POST'])
@login_required
def addTicket():
    if current_user.admin:
        data = json.loads(request.data)
        if 'user-id' in data:
            user_id = data["user-id"]
            user = User.query.get(user_id)

            try:
                new_event = Event(confirmed=False, user_id=current_user.id)
                db.session.add(new_event)
                db.session.commit()

                decrement_seat_number(1)

            except:
                flash("ACHTUNG! Ticket konnte nicht hinzugefügt werden!", category='error')

            return jsonify()

    return False


@views.route('/email')
def email():
    return render_template("email.html")
from flask import Blueprint, render_template, flash, jsonify
from flask_login import current_user, login_required
from .getSeatNumber import get_seat_number

views = Blueprint('views', __name__)


@views.route('/get-seat', methods=['POST'])
def getSeatId():
    s = get_seat_number()
    return jsonify(seat_number=s)



@views.route('/reservierung', methods=['GET', 'POST'])
@login_required
def reservierung():
    return render_template("reservierung.html")
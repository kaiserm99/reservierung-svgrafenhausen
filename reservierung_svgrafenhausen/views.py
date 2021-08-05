from flask import Blueprint, render_template, flash, jsonify
from flask_login import current_user
from .getSeatNumber import get_seat_number

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
    s = get_seat_number()
    return render_template("home.html", seat_number=s)

@views.route('/get-seat', methods=['POST'])
def getSeatId():
    s = get_seat_number()
    return jsonify(seat_number=s)

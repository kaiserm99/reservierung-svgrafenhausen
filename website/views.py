from flask import Blueprint, render_template, flash
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
    return render_template("home.html", user=current_user, active="home")
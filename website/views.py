from flask import Blueprint, render_template,request,flash,redirect,url_for,jsonify,send_from_directory
from flask_login import login_required, current_user
import os

from .models import Flag

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    flag_found = Flag.query.filter_by(id_user=current_user.id)
    return render_template("home.html", user=current_user, flags = flag_found)


        
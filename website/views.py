from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from .models import Flag
import os

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    flag_found = Flag.query.filter_by(id_user=current_user.id)
    return render_template("home.html", user=current_user, flags = flag_found)

@views.route('/admin', methods=['GET'])
@login_required
def admin():
    if(current_user.est_admin):
        flash("Bonjour cher admin", category='success')
        infos = []
        with open(os.path.abspath(os.path.dirname(__file__))+'/static/info','r') as f:
            infos = f.readlines()
        print(infos)
        return render_template("admin.html", user=current_user, infos=infos)
    else:
        flash("T'es pas admin toi non mais oh", category='error')
        return render_template("home.html", user=current_user)
        
from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from .models import Flag
import os
from . import db
from werkzeug.security import check_password_hash

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    flag_found = Flag.query.filter_by(id_user=current_user.id)
    if request.method == 'POST':
        testflag = request.form.get('flag')
        found = False
        for flag in flag_found:
            if check_password_hash(flag.hash, testflag):
                found = True
                flag.found = True
                db.session.commit()
                break   
        if(found):
            flash("Bien joué c'est un flag", category='success')
        else:
            flash("Raté cherches encore", category='error')

    all_ok = True
    for flag in flag_found:
        if(not flag.found):
           all_ok=False
           break
    return render_template("home.html", user=current_user, flags = flag_found, all = all_ok)

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
        
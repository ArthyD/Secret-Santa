from flask import Blueprint, render_template,request,flash,redirect,url_for
from .models import User, Flag
import os
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
hash_method = 'sha256'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nom = request.form.get('nom')
        password = request.form.get('password')

        user = User.query.filter_by(nom=nom).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash("Vous n'avez pas de compte", category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':

        nom = request.form.get('nom')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        isadmin = request.form.get('admin') or "False"

        user = User.query.filter_by(nom=nom).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(nom) < 4:
            flash('Nom trop court', category='error')

        elif password1 != password2:
            flash('Les mots de passes sont différents', category='error')
        elif len(password1) < 7:
            flash('Mot de passe trop court', category='error')
        else:
            new_user = User(nom=nom,
                            password=generate_password_hash(
                                password1),
                            est_admin=eval(isadmin))
            db.session.add(new_user)
            db.session.commit()
            init_flags(new_user)
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

def init_flags(user):
    flaglist=[]
    with open(os.path.abspath(os.path.dirname(__file__))+'/static/flags','r') as f:
        flaglist=f.readlines()
    print(flaglist)
    flag0 = Flag(nom="Echauffement", hash = flaglist[0], found=False, id_user=user.id)
    db.session.add(flag0)
    flag1 = Flag(nom="L'admin a perdu son chat", hash = flaglist[1], found=False, id_user=user.id)
    db.session.add(flag1)
    flag2 = Flag(nom="!--", hash = generate_password_hash(flaglist[2]), found=False, id_user=user.id)
    db.session.add(flag2)
    flag3 = Flag(nom="git add --all && git commit -m '' && git push && git oops", hash = generate_password_hash(flaglist[3]), found=False, id_user=user.id)
    db.session.add(flag3)

    
    db.session.commit()
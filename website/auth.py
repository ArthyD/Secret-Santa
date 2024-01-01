from flask import Flask,Blueprint, render_template,request,flash,redirect,url_for,jsonify
from .models import db,User
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
hash_method = 'sha256'
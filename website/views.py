from flask import Blueprint, render_template,request,flash,redirect,url_for,jsonify,send_from_directory

views = Blueprint('views', __name__)
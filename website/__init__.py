from flask import Flask,render_template
import os
import pwd
import sys
import uuid
import typing as t
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import werkzeug.debug

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")
    
    app.config['SECRET_KEY'] = 'This is a secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    user = pwd.getpwuid(os.getuid())[0]
    modname = getattr(app, "__module__", t.cast(object, app).__class__.__module__)
    mod = sys.modules.get(modname)
    app_name = getattr(app, "__name__", type(app).__name__)
    mod_file_loc = getattr(mod, '__file__', None)
    mac_addr = str (uuid.getnode ())
    machine_id = werkzeug.debug.get_machine_id()

    infostring = f"User: {user}\nModule: {modname}\nModule Name: {app_name}\nApp Location: {mod_file_loc}\nMac Address: {mac_addr}\nWerkzeug Machine ID: {machine_id}\n"
    with open(os.path.abspath(os.path.dirname(__file__))+'/static/info','w') as f:
        f.write(infostring)
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        

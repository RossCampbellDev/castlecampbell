from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "blogs.db"

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "such a secret key"
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.static_folder = 'static'
	db.init_app(app)

	from .views import views
	from .models import Post,User
	from .auth import auth

	app.register_blueprint(views, url_prefix="/")
	app.register_blueprint(auth, url_prefix="/")

	create_database(app)

	login_manager = LoginManager()
	login_manager.login_view = "auth.login"
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists("castle/" + DB_NAME):
		db.create_all(app=app)
		print("Created DB")

from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")

		user = User.query.filter_by(username=username).first()
		if user:
			if check_password_hash(user.password, password):
				login_user(user, remember=True)
				redirect(url_for('views.index'))
			else:
				flash('Password incorrect.', category='error')
		else:
			flash('Username incorrect.', category='error')

	return render_template("login.html", user=current_user)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")
	
		user = User.query.filter_by(username=username).first()
		if user is not None:
			return render_template("signup.html", user='')

		if username == '' or password=='':
			flash('Form incomplete.', category='error')
		else:
			user = User(username=username, password=generate_password_hash(password, method='sha256'))
			print("new user added " + username + ", " + password)
			db.session.add(user)
			db.session.commit()
			return render_template("login.html", user=user)
	
	return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for("views.index"))

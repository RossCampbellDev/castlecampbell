from flask import Blueprint, request, flash, render_template, url_for, redirect
from flask_login import login_required, current_user
from .weathergetter import get_weather
from .models import Post
from . import db
import datetime

weather_data = get_weather()

views = Blueprint("views", __name__)

@views.route("/")
def index():
	return render_template("index.html", weather=weather_data, user=current_user)


@views.route("/gitlines")
def gitlines():
	return render_template("gitlines.html", weather=weather_data, user=current_user)


@views.route("/writings")
def writings():
	return render_template("writings.html", weather=weather_data, user=current_user)


@views.route("/opinions")
def opinions():
	# posts = Post.query.all()
	posts = Post.query.filter_by().order_by(Post.datecreated.desc())
	return render_template("opinions.html", weather=weather_data, posts=posts, user=current_user)


@views.route("/opinions/<titleIn>")
def blog_post(titleIn):
	postobj = Post.query.filter_by(title=titleIn).first()
	return render_template("blogpost.html", weather=weather_data, post=postobj, user=current_user)


@views.route("/writeblog", methods=['GET', 'POST'])
@login_required
def write_blog():
	if request.method == "POST":
		title = request.form.get('title')
		body = request.form.get('body')
		datec = request.form.get('datecreated')
		if datec is not '' :
			dat = request.form.get('datecreated')
			y,m,d = dat.split(' ')[0].split('-')
			h,mm,s = dat.split(' ')[1].split(':')
			datecreated = datetime.datetime(int(y),int(m),int(d),int(h),int(mm),int(s))
			post = Post(title=title, body=body, datecreated=datecreated)
		else:
			post = Post(title=title, body=body)

		db.session.add(post)
		db.session.commit()
	else:
		return render_template("writeblog.html")

	return render_template("writeblog.html")


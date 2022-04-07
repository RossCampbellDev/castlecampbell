from flask import Blueprint, request, flash, render_template, url_for, redirect
from flask_login import login_required, current_user
from .weathergetter import get_weather
from .models import Post, User, Comment
from . import db
import datetime, os

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
	inc = True
	postobj = Post.query.filter_by(title=titleIn).first()
	if current_user.is_authenticated and current_user.id == 1:
		inc = False 

	if inc:
		viewcount = postobj.views
		viewcount = viewcount + 1
		postobj.views = viewcount
		db.session.commit()

	return render_template("blogpost.html", weather=weather_data, post=postobj, user=current_user)


@views.route("/newcomment", methods=['GET', 'POST'])
@login_required
def new_comment():
	if request.method == "POST":
		txt = request.form.get('newcomment')
		pid = request.form.get('pid')
		
		with open('/usr/share/nginx/castlesite/castle/static/bad-words.txt', 'r') as f:
			for word in f.readlines():
				print(word.replace('\n', ''))
				if word.replace('\n', '') in txt:
					flash('NO!  No naughty words!', "error")
					return redirect(url_for('views.flash_route'))

		cmt = Comment(text=txt, user_id=current_user.id, post_id=pid)
		db.session.add(cmt)
		db.session.commit()

	postobj = Post.query.filter_by(id=request.form.get('pid')).first()
	return render_template("blogpost.html", weather=weather_data, post=postobj, user=current_user)


@views.route("/deletecomment/<cid>")
@login_required
def delete_comment(cid):
	cmt = Comment.query.filter_by(id=cid).first()
	db.session.delete(cmt)
	db.session.commit()
	return redirect(url_for('views.index'))


@views.route("/writeblog", methods=['GET', 'POST'])
@login_required
def write_blog():
	if current_user.id != 1:
		return index()

	if request.method == "POST":
		title = request.form.get('title')
		body = request.form.get('body')
		datec = request.form.get('datecreated')
		if datec is not '' :
			dat = request.form.get('datecreated')
			y,m,d = dat.split(' ')[0].split('-')
			h,mm,s = dat.split(' ')[1].split(':')
			datecreated = datetime.datetime(int(y),int(m),int(d),int(h),int(mm),int(s))
			post = Post(title=title, body=body, datecreated=datecreated, views=0)
		else:
			post = Post(title=title, body=body, views=0)

		db.session.add(post)
		db.session.commit()
	else:
		return render_template("writeblog.html", user=current_user, post=None)

	return render_template("writeblog.html", user=current_user, post=None)

@views.route("/writeblog/<titleIn>", methods=['GET', 'POST'])
@login_required
def edit_blog(titleIn):
	if current_user.id != 1:
		return index()

	postobj = Post.query.filter_by(title=titleIn).first()

	if request.method == "POST":
		postobj.title = request.form.get('title')
		postobj.body = request.form.get('body')
		db.session.commit()

	return render_template("writeblog.html", post=postobj, user=current_user)


@views.route("/flash")
def flash_route():
	return render_template("flash.html", user=current_user, weather=weather_data)

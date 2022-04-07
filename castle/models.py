from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(256), unique=True)
	postcomments = db.relationship('Comment', backref='user', passive_deletes=True)
	chatcomments = db.relationship('ChatComment', backref='user', passive_deletes=True)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), unique=True, nullable=False)
	body = db.Column(db.String(50000), nullable=False)
	datecreated = db.Column(db.DateTime(timezone=True), default=func.now())
	views = db.Column(db.Integer)
	comments = db.relationship('Comment', backref='post', passive_deletes=True)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(500), nullable=False)
	datecreated = db.Column(db.DateTime(timezone=True), default=func.now())
	post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


class ChatComment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200), nullable=False)
	datecreated = db.Column(db.DateTime(timezone=True), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)

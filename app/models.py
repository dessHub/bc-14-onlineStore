import datetime
from app import db

class User(db):
	email = db.StringField(unique=True)
	password = db.StringField(default=True)
	username = db.StringField(unique=True)
	first_name = db.StringField()
	last_name = db.StringField()
	timestamp = db.DateTimeField(default=datetime.datetime.now())


class Note(db):
    title = db.StringField(required=True,max_length=120)
    content = db.StringField()
    last_updated = db.DateTimeField(default=datetime.datetime.now())
    user = db.ReferenceField(User)

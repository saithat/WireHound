from wrhnd import db, create_app
#from flask_login import UserMixin, login_manager

# required by the login manager
#@login_manager.user_loader()
#def load_user(user_id):
#	return User.query.get(int(user_id))

# Sample user class
#class User(db.Model, UserMixin):
class User(db.Model):
	ipaddress = db.Column(db.String(20), primary_key=True)
	geolocation = db.column(db.String(60), unique=True, nullable=False)
	strength = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return "User({}, {})".format(self.id, self.username)

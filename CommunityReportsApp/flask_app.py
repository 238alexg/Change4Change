# communityReportsApp.py

import flask
from flask import Flask, request, url_for, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from datetime import datetime
import json
import logging
import CONFIG
import uuid

###############
### Globals ###
###############
app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid4())
app.debug = CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)

# Database Globals
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="change4change",
    password="noSleep69",
    hostname="change4change.mysql.pythonanywhere-services.com",
    databasename="change4change$reports",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

###############
### Routes  ###
###############

# Test function to test database interaction
# LATER: Will have admin authentication, then various
#        queries to show reports.
@app.route("/displayReports", methods=['GET','POST'])
def displayReports():
    results = Report.query.all()
    return render_template('DBtest.html', results = results)

@app.route("/", methods=['GET','POST'])
def login():=
	# User is trying to log in to Google
	if (request.method == 'POST'):
		token = request.form.get('token')
<<<<<<< HEAD
		print(token)
		return render_template('map.html')
=======
		user = Users.query.filter(User.token == token)

		if (user == None):
			newUser = User(token = token)
			db.session.add(newUser)
			db.session.commit()
			user = Users.query.filter(User.token == token)
>>>>>>> 3a86dd1032235169b2b50a586dd9920723d1bb52

		session['token'] = token

	return render_template('signIn.html')

@app.route("/report", methods=['GET','POST'])
def report():
	# If user is directed to the report page
	if (request.method == 'GET'):
		return render_template('report.html')
	# If the user has posted a report form
	else:
		latitude = request.form.get('latitude')
		longitude = request.form.get('longitude')
		reportText = request.form.get('reportText')
		isEmergency = request.form.get('isEmergency')
		isAnonymous = request.form.get('isAnonymous')

		user = User.query.filter(User.token == session["token"])

		if (user == None):
			return render_template('error.html', error="No user in system!")

		# Create new report row
		newReport = Report(
			latitude = latitude,
			longitude = longitude,
			event_dt = datetime.now(),
			text = reportText,
			isEmergency = isEmergency,
			isAnonymous = isAnonymous,
			user = user
		)

		db.session.add(newReport)
		db.session.commit()

		# Render report page with report confirmation
		return render_template('report.html', success = True)



@app.route("/mapFile")
def mapFile():
    return flask.render_template('map.html')

@app.route("/signIn")
def signIn():
    return flask.render_template('signIn.html')


###############
### Models  ###
###############

# Database model declaration for report data
class Report(db.Model):
	__tablename__ = "reports"
	id = db.Column(db.Integer, primary_key = True)

	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	event_dt = db.Column(db.DateTime)
	text = db.Column(db.String(4096))
	isEmergency = db.Column(db.Boolean)
	isAnonymous = db.Column(db.Boolean)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship("User", back_populates="reports")

# Model for users
class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key = True)

	token = db.Column(db.String(1024), unique = True)
	reports = relationship("Report", back_populates="user")


if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug = CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT,threaded=True)

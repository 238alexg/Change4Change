# app.py for Change4Change
import flask
from flask import Flask, request, url_for, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

import json
import logging
import CONFIG
import uuid

###
# Globals
###
app = flask.Flask(__name__)

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

app.secret_key = str(uuid.uuid4())
app.debug = CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)


#############
####Pages####
#############

### Home Page ###
@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def index():
	if (request.method == 'GET'):
	    app.logger.debug("Main page entry")
	    return flask.render_template('index.html')

# Test function to test database interaction
# LATER: Will have admin authentication, then various 
#        queries to show reports.
def displayReports():
	return flask.render_template('displayReports.html', reports = Report.query.all())


# Database model declaration for report data
class Report(db.Model):
	__tablename__ = "reports"

	id = db.Column(db.Integer, primary_key = True)

	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	event_dt = db.Column(db.DateTime)
	text = db.Column(db.String(4096))
	isEmergency = db.Column(db.Boolean)

    
if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug = CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT,threaded=True)




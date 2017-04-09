# Initializes DB, creates 3 test reports, and commits them to the database
# WARNING: Calling this file will also REinitialize the database, dropping
#          all existing rows.

from flask_app import Report, User, db
from datetime import datetime

db.drop_all()
db.create_all()

# Create users
user1 = User(
	token = "THISISALONGTOKEN"
)

user2 = User(
	token = "THISISALSOALONGTOKEN"
)

# Create reports
report1 = Report(
	latitude = float(44.049228),
	longitude = float(123.092448),
	event_dt = datetime.now(),
	text = "This is my very first report!",
	isEmergency = False,
	isAnonymous = True,
	user = user1
)

report2 = Report(
	latitude = float(44.049238),
	longitude = float(123.092428),
	event_dt = datetime.now(),
	text = "Emergency! Help!",
	isEmergency = True,
	isAnonymous = False,
	user = user1
)

report3 = Report(
	latitude = float(44.049238),
	longitude = float(123.092428),
	event_dt = datetime.now(),
	text = "Positive comment, in same place as emergency",
	isEmergency = False,
	isAnonymous = False,
	user = user2
)


db.session.add(user1)
db.session.add(user2)
db.session.add(report1)
db.session.add(report2)
db.session.add(report3)

db.session.commit()
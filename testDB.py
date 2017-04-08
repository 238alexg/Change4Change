# Initializes DB, creates 3 test reports, and commits them to the database

from app import Report, db
from datetime import datetime

db.create_all()

report1 = Report(
	latitude = 44.049228,
	longitude = 123.092448,
	event_dt = datetime.now(),
	text = "This is my very first report!"
	isEmergency = False
)

report2 = Report(
	latitude = 44.049238,
	longitude = 123.092428,
	event_dt = datetime.now(),
	text = "Emergency! Help!"
	isEmergency = True
)

report3 = Report(
	latitude = 44.049238,
	longitude = 123.092428,
	event_dt = datetime.now(),
	text = "Positive comment, in same place as emergency"
	isEmergency = False
)

db.session.add(report1)
db.session.add(report2)
db.session.add(report3)
db.session.commit()
from app import Report, db
from datetime import datetime

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

db.session.add(report1)
db.session.add(report2)
db.session.commit()
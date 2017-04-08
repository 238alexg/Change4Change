from app import Report, db
from datetime import datetime

report1 = Report(
	latitude = 44.049228
	longitude = 123.092448
	event_dt = datetime.now()
	text = "This is my very first report!"
)
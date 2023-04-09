#Convert string to date time
import datetime
def convert(date_time):
	format = '%b %d %Y %I:%M%p' 
	datetime_str = datetime.datetime.strptime(date_time, format)

	return datetime_str
date_time = 'Apr 9 2023 10:07pM'
print(convert(date_time))

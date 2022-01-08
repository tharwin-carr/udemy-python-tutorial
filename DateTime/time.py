'''
Working with Time!
'''

import datetime

date_time = datetime.datetime(2022, 1, 7, 10, 58)
#move forward with time delta
# time_delta = datetime.timedelta(days=10)
# print(date_time + time_delta)

# Convert a string date to a date object
date_string = '2022-01-07'
date_object = datetime.date.fromisoformat(date_string)
time_delta = datetime.timedelta(days=5)
print(date_object + time_delta)
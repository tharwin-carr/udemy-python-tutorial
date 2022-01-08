'''
Working w/Dates!
'''

import datetime

#Today's Date

today = datetime.date.today()
# .weekday- Monday = 0, Sunday = 6
# .isoweekday - Monday = 1, Sunday = 7

# create_day = datetime.date(2022, 7, 21)

# How close are we to the new year?
new_year = datetime.date(2023, 1, 1)
days_remaining = new_year - today
print(days_remaining)
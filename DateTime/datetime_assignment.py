import datetime

today = datetime.date.today()
my_birthday = datetime.date(2022, 7, 21)

# How many days until my birthday?
days_remaining_until_birthday = my_birthday - today

delta_date = datetime.timedelta(days=20)
print(today + delta_date)

today_string = "2020-12-04"

date_object = datetime.date.fromisoformat(today_string)
print(date_object)
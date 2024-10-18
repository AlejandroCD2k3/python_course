from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

# -------------------- DATETIME --------------------

now = datetime.now()
year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(year_2023)

print(year_2023-now)

# -------------------- TIME --------------------

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.min)
print(current_time.second)

# -------------------- DATE --------------------

current_date = date.today()

print(current_date.min)
print(current_date.year)
print(current_date.month)
print(current_date.weekday())

current_date = date(2022, 10, 6)

print(current_date)

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)
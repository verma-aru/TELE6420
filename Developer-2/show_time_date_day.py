# show_time_date_day.py

import datetime

now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
current_day = now.strftime("%A")

print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")
print(f"Current Day: {current_day}")
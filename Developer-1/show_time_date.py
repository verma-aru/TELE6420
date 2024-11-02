# show_time_date.py

import datetime

now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")


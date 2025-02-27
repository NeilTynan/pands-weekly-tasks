import datetime
import calendar
from datetime import date

# Weekday/Weekend checker programme
def check_weekday_or_weekend(today):
    
    day_of_week = (today.weekday())   # Convert Sunday from 6 to 0
         
    if day_of_week < 4:
        day_type = 'weekday'
        print(f"Bad news, today is a {day_type}")
    else:
        day_type = 'weekend'
        print(f"Good news, today is the {day_type}")

# Enter in today's date
today = date.today()

# Check if today is a weekday or if it's the weekend:
check_weekday_or_weekend(today)
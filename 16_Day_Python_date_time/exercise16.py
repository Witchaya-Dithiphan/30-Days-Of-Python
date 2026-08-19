# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime, date

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
time_stamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp: ",time_stamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)

# Today is 5 December, 2019. Change this time string to time.

today_string = "5 December, 2019"
print(today_string)
today_object = datetime.strptime(today_string,"%d %B, %Y")
print(today_object)

# Calculate the time difference between now and new year.

today = now.date()
new_year = date(year=2026, month=1, day=1)

diff = today - new_year
print('Time difference between now and new year:', diff)

# Calculate the time difference between 1 January 1970 and now.

that_day = date(year=1970, month=1, day=1)
diff = today - that_day
print('Time difference between now and 1 January 1970:', diff)

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog

# using datetime to log order timestamps is an essential part of building a backtest engine. In a BTC/USD backtester, precision, timezone awareness, and speed execution tracking are critical.
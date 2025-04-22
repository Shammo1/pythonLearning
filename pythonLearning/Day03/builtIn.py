from random import*
print(randint(1,6))
##https://docs.python.org/3/py-modindex.html
from time import localtime
current_time = localtime()
hour = current_time.tm_hour
if hour > 12:
    hour -= 12
    period = "PM"
else:
    period = "AM"

print(f"Hour: {hour} Minute: {current_time.tm_min} {period}")
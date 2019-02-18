"""
Problem
You have code that needs to perform simple time conversions, like days to seconds,
hours to minutes, and so on.
"""

# Solution
# To perform conversions and arithmetic involving different units of time, use the date
# time module. For example, to represent an interval of time, create a timedelta instance,
# like this:

from datetime import timedelta
from datetime import datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days, c.seconds, c.seconds / 3600, c.total_seconds() / 3600)

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# To illustrate, many similar time calculations can be performed with the dateutil.rel
# ativedelta() function.

a = datetime(2012, 9, 23)
# print(a + timedelta(months=1))
# TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta

print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

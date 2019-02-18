"""
Problem
You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At
what local time did your friend in Bangalore, India, have to show up to attend?
"""

# Solution
# For almost any problem involving time zones, you should use the pytz module. This
# package provides the Olson time zone database, which is the de facto standard for time
# zone information found in many languages and operating systems.

from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
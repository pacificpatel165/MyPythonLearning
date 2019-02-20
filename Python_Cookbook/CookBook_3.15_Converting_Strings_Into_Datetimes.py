"""
Problem
Your application receives temporal data in string format, but you want to convert those
strings into datetime objects in order to perform nonstring operations on them.
"""

# Solution
# Python’s standard datetime module is typically the easy solution for this. For example:

from datetime import datetime

text = '2019-01-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
z = datetime.now()
print(z)
diff = z - y
print(diff)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

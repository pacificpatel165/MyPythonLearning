"""
Problem
You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
transform or filter the data.
"""

# Solution
# A very elegant way to combine a data reduction and a transformation is to use a
# generator-expression argument.

nums = [1, 2, 3, 4, 5]
print(sum(n * n for n in nums))


# Determine if any .py files exist in a directory
import os

files = os.listdir('C:/Users/prpatel.CORP/PycharmProjects/MyPythonLearning/Python_Cookbook')

if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

# Original: Returns 20
print(min(s['shares'] for s in portfolio))

# Alternative: Returns {'name': 'AOL', 'shares': 20}
print(min(portfolio, key=lambda s: s['shares']))


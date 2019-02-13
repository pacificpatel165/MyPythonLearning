"""
Problem
You want to search for and replace a text pattern in a string.
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yep'))

text = 'Today is 02/12/2019. PyCon starts 3/13/2019.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date, text))
"""
Problem
You want to match or search text for a specific pattern.
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

text1 = '02/12/2019'
text2 = 'Feb 12, 2019'

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# If you’re going to perform a lot of matches using the same pattern, it usually pays to
# precompile the regular expression pattern into a pattern object first.

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() always tries to find the match at the start of a string. If you want to search text
# for all occurrences of a pattern, use the findall() method instead.

text = 'Today is 02/12/2019. PyCon starts 3/13/2019.'
print(datepat.findall(text))

# When defining regular expressions, it is common to introduce capture groups by enclosing
# parts of the pattern in parentheses.

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('02/12/2019')
print(m)

# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
print(text)
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(month, day, year))

for m in datepat.finditer(text):
    print(m.groups())

# Be aware that the match() method only checks the beginning of a string. It’s possible
# that it will match things you aren’t expecting.
m = datepat.match('02/12/2019abcdef')
print(m.groups())

# If you want an exact match, make sure the pattern includes the end-marker ($)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match('02/12/2019abcdef')
if m != None:
    print(m.groups())
else:
    print('No match')
m = datepat.match('02/12/2019')
print(m.groups())
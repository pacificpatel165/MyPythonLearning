"""
Problem
You need to split a string into fields, but the delimiters (and spacing around them) aren’t
consistent throughout the string.
"""

# Solution
# The split() method of string objects is really meant for very simple cases, and does
# not allow for multiple delimiters or account for possible whitespace around the delimiters.

import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(line.split(' '))

# The separator is either a comma (,), semicolon (;), or whitespace followed by any amount of extra whitespace.
print(re.split(r'[;,\s]\s*', line))
# Or other way
print(re.split(r'(?:;|,|\s)\s*', line))

# Be careful, below regular expression generate different output
print(re.split(r'(;|,|\s)\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)

# Reform the line using the same delimiters
print(''.join(v+d for v, d in zip(values, delimiters)))


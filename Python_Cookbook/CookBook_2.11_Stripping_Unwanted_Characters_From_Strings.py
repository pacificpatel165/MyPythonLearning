"""
Problem
You want to strip unwanted characters, such as whitespace, from the beginning, end, or
middle of a text string.
"""

# Solution
# The strip() method can be used to strip characters from the beginning or end of a
# string. lstrip() and rstrip() perform stripping from the left or right side, respectively.
# By default, these methods strip whitespace, but other characters can be given.

# Whitespace stripping
s = ' hello world \n'

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='

print(t.lstrip('-'))
print(t.strip('-='))

# Be aware that stripping does not apply to any text in the middle of a string.
s = ' hello     world    '
print(s.strip())

# If you needed to do something to the inner space, you would need to use another technique,
# such as using the replace() method or a regular expression substitution.
print(s.replace(' ', ''))

import re
print(re.sub('\s+', ' ', s))
print(re.sub('\s+', ' ', s).strip())



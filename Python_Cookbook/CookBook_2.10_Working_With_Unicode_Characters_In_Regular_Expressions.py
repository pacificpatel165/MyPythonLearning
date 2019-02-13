"""
Problem
You are using regular expressions to process text, but are concerned about the handling
of Unicode characters.
"""

# Solution
# By default, the re module is already programmed with rudimentary knowledge of certain
# Unicode character classes. For example, \d already matches any unicode digit
# character:

import re

num = re.compile('\d+')

# ASCII digits
print(num.match('123'))

# Arabic digits
print(num.match('\u0661\u0662\u0663'))

# If you need to include specific Unicode characters in patterns, you can use the usual
# escape sequence for Unicode characters (e.g., \uFFFF or \UFFFFFFF).
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))             # Matches
print(pat.match(s.upper()))     # Doesn't match
print(s.upper())

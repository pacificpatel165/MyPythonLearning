"""
Problem
You’re trying to match a text pattern using regular expressions, but it is identifying the
longest possible matches of a pattern. Instead, you would like to change it to find the
shortest possible match.
"""

# Solution
# This problem often arises in patterns that try to match text enclosed inside a pair of
# starting and ending delimiters (e.g., a quoted string).

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# In above example, the pattern r'\"(.*)\"' is attempting to match text enclosed inside
# quotes. However, the * operator in a regular expression is greedy, so matching is based
# on finding the longest possible match.

# To fix this, add the ? modifier after the * operator in the pattern, like this
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))



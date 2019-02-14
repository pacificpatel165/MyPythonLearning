"""
Problem
You have long strings that you want to reformat so that they fill a user-specified number
of columns.
"""

# Solution
# Use the textwrap module to reformat text for output. For example, suppose you have
# the following long string:

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))




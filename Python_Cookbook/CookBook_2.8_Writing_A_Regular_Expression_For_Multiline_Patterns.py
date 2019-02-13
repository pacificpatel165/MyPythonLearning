"""
Problem
You’re trying to match a block of text using a regular expression, but you need the match
to span multiple lines.
"""

# Solution
# This problem typically arises in patterns that use the dot (.) to match any character but
# forget to account for the fact that it doesn’t match newlines.

import re

comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a
         multiline comment */
        '''
print(comment.findall(text1))
print(comment.findall(text2))

# To fix the problem, you can add support for newlines.
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes
# the . in a regular expression match all characters, including newlines.

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

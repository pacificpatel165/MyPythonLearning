"""
Problem
You want to replace HTML or XML entities such as &entity; or &#code; with their
corresponding text. Alternatively, you need to produce text, but escape certain characters
(e.g., <, >, or &).
"""

# Solution
# If you are producing text, replacing special characters such as < or > is relatively easy if
# you use the html.escape() function. For example:

import html

s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))


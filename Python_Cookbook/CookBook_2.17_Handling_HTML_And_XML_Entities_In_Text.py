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

# If you’re trying to emit text as ASCII and want to embed character code entities for non-
# ASCII characters, you can use the errors='xmlcharrefreplace' argument to various
# I/O-related functions to do it.

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'

from html.parser import HTMLParser

p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'

from xml.sax.saxutils import unescape

print(unescape(t))
"""
Problem
You want to perform common text operations (e.g., stripping, searching, and replacement)
on byte strings.
"""

# Solution
# Byte strings already support most of the same built-in operations as text strings. For
# example:

data = b'Hello World'

print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')

print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# You can apply regular expression pattern matching to byte strings, but the patterns
# themselves need to be specified as bytes.

data = b'FOO:BAR,SPAM'

import re

# print(re.split('[:,]',data))  # it will throw error
print(re.split(b'[:,]',data))   # Notice: pattern as bytes


# Difference in plain text string and byte string

a = 'Hello World' # Text string
print(a[0], a[1])

b = b'Hello World' # Byte string
print(b[0], b[1])

s = b'Hello World'
print(s)    # Observe b'...'
print(s.decode('ascii'))
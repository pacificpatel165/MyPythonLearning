"""
Problem
You need to check the start or end of a string for specific text patterns, such as filename
extensions, URL schemes, and so on.
"""

# Solution
# A simple way to check the beginning or end of a string is to use the str.starts
# with() or str.endswith() methods.

filename = 'spam.txt'
print(filename.endswith('txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

print(filename[-4:] == '.txt')
print(url[:5] == 'http:' or url[:6] == 'htpps:' or url[:4] == 'ftp:')

import re

print(re.match('http:|https:|ftp:', url))

import os

filenames = os.listdir('.')
# print(filenames)

print([name for name in filenames if name.endswith('.txt')])
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))
print(url.startswith(tuple(choices)))

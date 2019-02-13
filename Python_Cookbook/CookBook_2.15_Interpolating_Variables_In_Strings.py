"""
Problem
You want to create a string in which embedded variable names are substituted with a
string representation of a variable’s value.
"""

# Solution
# Python has no direct support for simply substituting variable values in strings. However,
# this feature can be approximated using the format() method of strings.

s = '{name} has {n} messages.'
print(s.format(name='Prashant', n=165))

# Alternatively, if the values to be substituted are truly found in variables, you can use the
# combination of format_map() and vars(), as in the following:

name = 'Patel'
n = 101
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('PP', 200)
print(s.format_map(vars(a)))

import sys


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('{name} has {n} messages.'))
print(sub('Your favorite color is {color}'))

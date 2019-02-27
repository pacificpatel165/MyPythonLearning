"""
Problem
You would like to define a generator function, but it involves extra state that you would
like to expose to the user somehow.
"""

# Solution
# If you want a generator to expose extra state to the user, don’t forget that you can easily
# implement it as a class, putting the generator function code in the __iter__() method.
# For example:

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

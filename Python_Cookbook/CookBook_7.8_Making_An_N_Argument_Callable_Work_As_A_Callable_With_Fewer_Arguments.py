"""
Problem
You have a callable that you would like to use with some other Python code, possibly as
a callback function or handler, but it takes too many arguments and causes an exception
when called.
"""

# Solution
# If you need to reduce the number of arguments to a function, you should use func
# tools.partial(). The partial() function allows you to assign fixed values to one or
# more of the arguments, thus reducing the number of arguments that need to be supplied
# to subsequent calls. To illustrate, suppose you have this function:

from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)  # a = 1
s1(2, 3, 4)
s1(4, 7, 9)

s2 = partial(spam, d=42)  # d = 42
s2(1, 2, 3)
s2(4, 5, 5)

s3 = partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42
s3(3)
s3(4)
s3(5)

# As a first example, suppose you have a list of points represented as tuples of (x,y) coordinates.
# You could use the following function to compute the distance between two
# points:

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


# Now suppose you want to sort all of the points according to their distance from some
# other point. The sort() method of lists accepts a key argument that can be used to
# customize sorting, but it only works with functions that take a single argument (thus,
# distance() is not suitable). Here’s how you might use partial() to fix it:

pt = (3, 4)
points.sort(key=partial(distance, pt))
print(points)

# For example, here’s a bit of code
# that uses multiprocessing to asynchronously compute a result which is handed to a
# callback function that accepts both the result and an optional logging argument:

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

# A sample function
def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

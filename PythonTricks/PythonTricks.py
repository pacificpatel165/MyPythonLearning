"""
Below programs are day to day python tricks
"""


# ==============================================================================
# """
# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)
myfunc(**dict_vec)
# """
# ==============================================================================
"""
# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)

# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
# json.dumps({all: 'yup'})
# TypeError: keys must be a string
"""
# ==============================================================================
"""
# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)

# We get a nice string repr for free:
print(my_car)
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
# my_car.color = 'blue'
# AttributeError: "can't set attribute"
"""
# ==============================================================================
"""
# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    print("Hi %s!" % name_for_userid.get(userid, "there"))

greeting(382)
greeting(333333)
"""
# ==============================================================================
"""
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
print(xs)

# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))
print(xs)
"""
# ==============================================================================
"""
# Different ways to test multiple
# flags at once in Python

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    pass
    #print('passed')

if 1 in (x, y, z):
    pass
    #print('passed')

# These only test for truthiness:
if x or y or z:
    pass
    #print('passed')

if any((x, y, z)):
    pass
    #print('passed')
"""

# ==============================================================================
"""
# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

#print(z)

# In Python 2.x you could
# use this:
z = dict(x, **y)
#print(z)

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
"""
# ==============================================================================

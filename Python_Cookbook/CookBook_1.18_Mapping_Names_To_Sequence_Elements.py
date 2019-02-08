"""
Problem
You have code that accesses list or tuple elements by position, but this makes the code
somewhat difficult to read at times. You’d also like to be less dependent on position in
the structure, by accessing the elements by name.
"""

# Solution
# collections.namedtuple() provides these benefits, while adding minimal overhead
# over using a normal tuple object. collections.namedtuple() is actually a factory
# method that returns a subclass of the standard Python tuple type.

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)


# It's not a good approach, because position can be change and need to modified the code
def compute_cost_position(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# Good approach, with help of namedtuple we discard the positional approach
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(a)
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(b)
print(dict_to_stock(b))

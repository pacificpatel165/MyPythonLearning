""""
Problem
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
"""

p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, mon, day) = data
print(year, mon, day)

_, shares, price, _ = data # Python use throwaway variable(_) name to discard certain values.



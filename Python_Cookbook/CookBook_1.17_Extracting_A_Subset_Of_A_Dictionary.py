"""
Problem
You want to make a dictionary that is a subset of another dictionary.
"""

# This is easily accomplished using a dictionary comprehension.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# Other way to do but slower
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# Other way to do but slower
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)
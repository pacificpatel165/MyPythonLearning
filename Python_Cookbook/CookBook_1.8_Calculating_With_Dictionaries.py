"""
Problem
You want to perform various calculations (e.g., minimum value, maximum value, sorting,
etc.) on a dictionary of data.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(min(prices))  # return key of dictionary
print(min(prices.values()))  # return value of dictionary
print(min(prices, key=lambda k: prices[k]))  # return key of dictionary who has minimum value
print(prices[min(prices, key=lambda k: prices[k])])  # First get the key of minimum value and then apply to get value

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# Be aware that zip() creates an iterator that can only be
# consumed once.
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

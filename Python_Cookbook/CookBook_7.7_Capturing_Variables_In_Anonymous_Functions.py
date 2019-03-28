"""
Problem
You’ve defined an anonymous function using lambda, but you also need to capture the
values of certain variables at the time of definition.
"""

# Solution
# Consider the behavior of the following code:

x = 10
a = lambda y: x + y

x = 20
b = lambda y: x + y

print(a(10))
print(b(10))

# Now ask yourself a question. What are the values of a(10) and b(10)? If you think the
# results might be 20 and 30, you would be wrong:

# The problem here is that the value of x used in the lambda expression is a free variable
# that gets bound at runtime, not definition time.

# Thus, the value of x in the lambda
# expressions is whatever the value of the x variable happens to be at the time of execution.
# For example:

x = 15
print(a(10))

x = 3
print(b(10))

# If you want an anonymous function to capture a value at the point of definition and
# keep it, include the value as a default value, like this:

x = 10
a = lambda y, x=x: x + y

x = 20
b = lambda y, x=x: x + y

print(a(10))
print(b(10))


# For example,
# creating a list of lambda expressions using a list comprehension or in a loop of some
# kind and expecting the lambda functions to remember the iteration variable at the time
# of definition. For example:

funcs = [lambda x: x + n for n in range(5)]

for f in funcs:
    print(f(0))

# Notice how all functions think that n has the last value during iteration. Now compare
# to the following:

funcs = [lambda x, n=n: x + n for n in range(5)]

for f in funcs:
    print(f(0))

# coding=utf-8
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
print(fact)
print(fact(5))

# A function that takes a function as argument or returns a function as result is a Higher Order Function
print(map(fact, range(11))) 
print(list(map(fact, range(11))))

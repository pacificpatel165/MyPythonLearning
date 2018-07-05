# coding=utf-8

"""A function may change any mutable object it receives."""


def f(a, b):
    a += b
    return a


x = 1
y = 2
print('Result = {}'.format(f(x, y)))
print('x = {} and y = {}'.format(x, y))

x = [1, 2]
y = [3, 4]
print('Result = {}'.format(f(x, y)))
print('x = {} and y = {}'.format(x, y))

x = (10, 20)
y = (30, 40)
print('Result = {}'.format(f(x, y)))
print('x = {} and y = {}'.format(x, y))

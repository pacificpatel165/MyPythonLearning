# coding=utf-8

"""A broken higher-order function to calculate a running average without
keeping all history."""

'''
def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager
'''
'''
>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
...
UnboundLocalError: local variable 'count' referenced before assignment
>>>
'''

'''The problem is that the statement count += 1 actually means the same as count =
count + 1, when count is a number or any immutable type. So we are actually assigning
to count in the body of averager, and that makes it a local variable. The same problem
affects the total variable.'''

"""A broken higher-order function to calculate a running average without
keeping all history."""


def make_averager3():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager3()
print(avg(10))
print(avg(11))
print(avg(12))

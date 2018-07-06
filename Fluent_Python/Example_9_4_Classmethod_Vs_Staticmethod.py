# coding=utf-8

"""Comparing behaviors or classmethod and staticmethod."""


class Demo:

    @classmethod
    def klassmeth(*args):
        return args  # klassmeth just returns all positional arguments.

    @staticmethod
    def statmeth(*args):
        return args  # statmeth does the same.


print(Demo.klassmeth())  # No matter how you invoke it, Demo.klassmeth receives the Demo class as the first argument.

print(Demo.klassmeth('spam'))

print(Demo.statmeth())  # Demo.statmeth behaves just like a plain old function.

print(Demo.statmeth('spam'))

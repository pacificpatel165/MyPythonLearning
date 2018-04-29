# coding=utf-8


""""Listing attributes of functions that don’t exist in plain instances."""


class C:
    pass


obj = C()


def func():
    pass


print(sorted(set(dir(func)) - set(dir(obj))))

print(sorted(set(dir(obj)) - set(dir(func))))

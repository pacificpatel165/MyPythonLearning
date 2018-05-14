# coding=utf-8


""""Sorting a list of words by their reversed spelling using lambda."""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word:word[::-1]))

# How to know if object is callable
print(abs, str, 13)
print([callable(obj) for obj in (abs, str, 13)])

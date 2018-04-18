"""Problem
    You want to implement a custom class that mimics the behavior of a common built-in
    container type, such as a list or dictionary. However, you’re not entirely sure what
    methods need to be implemented to do it.
"""
import collections
import bisect


class SortedItems(collections.Sequence):
    """
    Class for sorted items
    """
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))



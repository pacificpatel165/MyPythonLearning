"""
Problem
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return 'Item({!r})'.format(self._name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Object
a = Item('foo')
b = Item('bar')
#print(a < b)

# Priority, Object
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
c = (1, Item('grok'))
#print(a < c)

# Priority, Index, Object
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
print(a < b)
c = (1, 2, Item('grok'))
print(a < c)



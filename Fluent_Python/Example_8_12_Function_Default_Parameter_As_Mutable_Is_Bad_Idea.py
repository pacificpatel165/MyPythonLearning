# coding=utf-8

"""A simple class to illustrate the danger of a mutable default."""


class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)  # ['Alice', 'Bill']

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)  # ['Carrie']

bus3 = HauntedBus()
print(bus3.passengers)  # ['Carrie'] --> BAD
bus3.pick('Dave')
print(bus2.passengers)  # ['Carrie', 'Dave'] --> BAD

print(bus2.passengers is bus3.passengers)

print(bus1.passengers)

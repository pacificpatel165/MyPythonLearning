# Abstract Base Classes (ABCs)ensure that derived classes implementation
# particular methods from the bae class at instantiation time.

# Using ABCs can help avoid bugs and make class hierarchies easier to
# maintain.

class Base:
    def foo(self):
        raise 'NotImplementedError()'

    def bar(self):
        raise 'NotImplementedError()'


class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #   return 'bar() called'


b = Base()
# b.foo()

c = Concrete()
print(c.foo())
# c.bar()


# Using Abstract Base Class concept

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    # We forgot to declare bar() again ...


c = Concrete()

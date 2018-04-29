# coding=utf-8


""""Demo of methodcaller : second test shows the binding of extra argu‐ments."""

from operator import methodcaller


s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))


# The '==' operator compares by checking for 'equality'
# The 'is' operator, however, compares 'identities'.

a = [1, 2, 3]
b = a

print(a == b)
print(a is b)

c = list(a)
print(a == c)
print(a is c)

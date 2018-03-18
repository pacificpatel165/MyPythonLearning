# Build a set of Latin-1 characters that have the word “SIGN” in their Unicode names.

from unicodedata import name

print({chr(i) for i in range(32, 256)})
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

a = set()
#print(help(a))
#print(help(set.__class__))

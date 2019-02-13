"""
Problem
You’re working with Unicode strings, but need to make sure that all of the strings have
the same underlying representation.
"""

s1 = 'Spicy Jalape\u00f1o'   # Uses the fully composed “ñ” character (U+00F1)
s2 = 'Spicy Jalapen\u0303o'  # Uses the Latin letter “n” followed by a “~” combining character (U+0303)

print(s1)
print(s2)

print(s1 == s2)
print(len(s1))
print(len(s2))

# Having multiple representations is a problem for programs that compare strings. In
# order to fix this, you should first normalize the text into a standard representation using
# the unicodedata module:

import unicodedata

t1 = unicodedata.normalize('NFC', s1)  # NFC means characters should be fully composed
t2 = unicodedata.normalize('NFC', s2)
print(t1, t2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)  # NFD means that characters should be fully decomposed
t4 = unicodedata.normalize('NFD', s2)
print(t3, t4)
print(t3 == t4)
print(ascii(t4))

s = '\ufb01' # A single character
print(s)

print(unicodedata.normalize('NFD', s))

# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))
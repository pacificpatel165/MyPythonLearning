"""
Problem
Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page
and you’d like to clean it up somehow.
"""

# Solution
# Perhaps, for example, you want to eliminate whole ranges of characters or strip diacritical marks.
# To do so, you can turn to the often overlooked str.translate() method.

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# The first step is to clean up the whitespace. To do this, make a small translation table
# and use translate():
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None # Deleted
}

a = s.translate(remap)
print(a)

# You can take this remapping idea a step further and build much bigger tables. For example,
# let’s remove all combining characters:

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
# print(cmb_chrs)

b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# Yet another technique for cleaning up text involves I/O decoding and encoding functions.
# The idea here is to first do some preliminary cleanup of the text, and then run it
# through a combination of encode() or decode() operations to strip or alter it.

b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
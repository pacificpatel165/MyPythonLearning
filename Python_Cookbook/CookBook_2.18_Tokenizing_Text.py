"""
Problem
You have a string that you want to parse left to right into a stream of tokens.
"""

text = 'foo = 23 + 42 * 10'

# To tokenize the string, you need to do more than merely match patterns. You need to
# have some way to identify the kind of pattern as well.

# To do this kind of splitting, the first step is to define all of the possible tokens, including
# whitespace, by regular expression patterns using named capture groups such as this

import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
scan = scanner.match()
print((scan.lastgroup, scan.group()))

scan = scanner.match()
print((scan.lastgroup, scan.group()))

scan = scanner.match()
print((scan.lastgroup, scan.group()))

scan = scanner.match()
print((scan.lastgroup, scan.group()))

scan = scanner.match()
print((scan.lastgroup, scan.group()))

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner_ = pat.scanner(text)
    for m in iter(scanner_.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

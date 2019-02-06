"""
Problem
You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”).
"""

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : (1, 2, 3),
    'b' : (4, 5)
}

import json
print(json.dumps(d, indent=4, sort_keys=True))
print(json.dumps(e, indent=4, sort_keys=True))

from collections import defaultdict

dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['d'].append(4)
print(dl)

ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['d'].add(4)
print(ds)

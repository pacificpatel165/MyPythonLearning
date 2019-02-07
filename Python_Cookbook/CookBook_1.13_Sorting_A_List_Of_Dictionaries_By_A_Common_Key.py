"""
Problem
You have a list of dictionaries and you would like to sort the entries according to one
or more of the dictionary values.
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lname)

# Alternative way by using lambda
rows_by_lname = sorted(rows, key=lambda value: (value['lname'], value['fname']))
print(rows_by_lname)

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))

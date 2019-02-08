"""
Problem
You want to sort objects of the same class, but they don’t natively support comparison
operations.
"""


class User:
    def __init__(self, user_id):
        self._user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self._user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u._user_id))

from operator import attrgetter

print(sorted(users, key=attrgetter('_user_id')))

# coding=utf-8

"""Checking out the behavior of __getitem__ and slices."""

class MySeq:

    def __getitem__(self, index):
        return index


s = MySeq()
print(s[1])

print(s[1:4])

print(s[1:4:2])

print(s[1:4:2, 9])

print(s[1:4:2, 7:9])

print(slice)
print(dir(slice))

print(slice(None, 10, 2).indices(5))  # 'ABCDE'[:10:2] is the same as 'ABCDE'[0:5:2]
print(slice(-3, None, None).indices(5))  # 'ABCDE'[-3:] is the same as 'ABCDE'[2:5:1]

print('ABCDE'[:10:2])  # Or
print('ABCDE'[0:5:2])

print('ABCDE'[-3:])  # Or
print('ABCDE'[2:5:1])

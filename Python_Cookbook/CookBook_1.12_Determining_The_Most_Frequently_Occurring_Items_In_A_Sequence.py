"""
Problem
You have a sequence of items, and you’d like to determine the most frequently occurring
items in the sequence.
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

# Combine counts
c = a + b
print(c)

# Subtract counts
d = a - b
print(d)

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

word_counts.update(morewords)

sentence = "look into my eyes look into their eyes"
word_counts = Counter(sentence.split(' '))
print(word_counts)

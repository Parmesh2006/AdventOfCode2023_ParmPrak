#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from functools import reduce

# open and read the file
data = open('Day15\\input.txt').read().strip().split(',')

# calculate the hash of the character using the anonymous function method
char = lambda i, c: (i + ord(c)) * 17 % 256
hash = lambda s: reduce(char, s, 0)

# create a list to store the boxes
boxes = [dict() for _ in range(256)]

# for each step in the data, use the hashes to update the elements to the right box
for step in data:
    match step.strip('-').split('='):
        case [l, f]: 
            boxes[hash(l)][l] = int(f)
        case [l]:
            boxes[hash(l)].pop(l, 0)

# Print the total focusing power using the dictionary
print(sum(i * j * f for i, b in enumerate(boxes, 1)
                for j, f in enumerate(b.values(), 1)))
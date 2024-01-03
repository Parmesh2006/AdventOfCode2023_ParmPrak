#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

import collections as C, re

# Drops a specified stack in the stacks of bricks
def drop(stack, skip=None):
    # Track the peaks
    peaks = C.defaultdict(int)
    falls = 0

    # Go through each pair of points
    for i, (u, v, w, x, y, z) in enumerate(stack):
        # skip if necessary
        if i == skip: 
            continue

        # Track the areas the bricks cover
        area = [(a, b) for a in range(u, x + 1)
                       for b in range(v, y + 1)]
        
        # Find the peak
        peak = max(peaks[a] for a in area) + 1

        # Track the peaks in the defaultdict data structure
        for a in area: 
            peaks[a] = peak + z - w

        # Add the points to the stack
        stack[i] = (u, v, peak, x, y, peak + z - w)

        # Add the length of the fall to falls
        falls += peak < w

    # return whether the stack falls or not
    return not falls, falls

# Create the stack that is disintegrated
stack = sorted([[*map(int, re.findall(r'\d+',l))]
    for l in open('Day22\\input.txt')], key=lambda b:b[2])

# Drop the disintegrated stack
drop(stack)

# Prints Part 1 and Part 2 answers
print(*map(sum, zip(*[drop(stack.copy(), skip=i)
    for i in range(len(stack))])))
#!/usr/bin/python

import re
import math

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Open file and extract information
with open("Day8\\input.txt") as file:
    lines = [line.replace("\n", "") for line in file]

# Input all info from file into dictionary
directionDict = {}
for i, line in enumerate(lines):
    l = line.strip()
    if i == 0:
        directions = l
    elif i != 1:
        place, left, right = re.findall("\w+", l)
        directionDict[place] = (left, right)

# Set up the loop
stepCount = 0
place = 'AAA'
i = 0

while (place != 'ZZZ'):
    if i == len(directions):
        # reset i to start directions over
        i = 0
    
    currentMove = directions[i]

    # check if currentm ove is left or right
    if currentMove == 'L':
        place = directionDict[place][0]
    else:
        place = directionDict[place][1]

    # increment steps and i
    stepCount += 1
    i += 1

# Number of steps
print(stepCount)

"""
PART TWO IS BELOW
"""

# PART TWO
import collections

steps_to_z = collections.defaultdict(list)
def calc_dist(p):
    orig_p = p
    viz = set()
    steps = 0
    i = -1
    while True:
        if p[-1] == 'Z':
            steps_to_z[orig_p].append(steps)

        steps += 1

        i += 1
        if i == len(directions):
            i = 0
        
        move = directions[i]

        if (p, i) in viz:
            break

        viz.add((p, i))

        if move == 'L':
            p = directionDict[p][0]
        else:
            p = directionDict[p][1]

# Calculate the distance for each point in direction dictionary
for p in directionDict:
    if p[-1] == 'A':
        calc_dist(p)
    
# compare this set to all other sets, and get the least set
x = set()
for p in directionDict:
    if p[-1] == 'A':
        x |= set([int(x) for x in steps_to_z[p]])

print(math.lcm(*list(x)))
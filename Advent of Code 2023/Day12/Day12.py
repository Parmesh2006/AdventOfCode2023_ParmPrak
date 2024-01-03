#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from functools import cache

@cache
def recurse(lava, springs, result=0):
    # if springs is false, then check if no hashtags
    if not springs:
        return '#' not in lava
    
    # compare current and springs and check if there are gears in the lava
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        if (nxt := i + current) <= len(lava) and '.' not in lava[i : nxt] and lava[nxt : nxt + 1] != "#":
            result += recurse(lava[nxt + 1:], springs)
    
    # return result, which is the total number of combinations possible
    return result


with open("Day12\\input.txt", "r") as file:
    # preprocess the text
    data = [x.split() for x in file.read().splitlines()]

    # Use the recursive method above to solve the problems
    p1, p2 = 0, 0
    for e, (lava, springs) in enumerate(data):
        p1 += recurse(lava, (springs := tuple(map(int, springs.split(",")))))
        p2 += recurse("?".join([lava] * 5), springs * 5)

    # p1 is part 1, and p2 is part 2
    print(p1, p2)
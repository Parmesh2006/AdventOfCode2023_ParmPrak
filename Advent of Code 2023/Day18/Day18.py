#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

plan = list(map(str.split, open('Day18\\input.txt')))

# List the ways a direction will go in terms of coordinates
dirs = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1),
        '0': (1, 0), '1': (0, 1), '2': (-1 ,0), '3': (0, -1)}

# This function checks the number of steps from a certain position and calculates where you will end up
def f(steps, pos=0, ans=1):
    for (x,y), n in steps:
        pos += x * n
        ans += y * n * pos + n/2

    return int(ans)

# Answer to first one and second one
print(f((dirs[d],    int(s))          for d,s,_ in plan),
      f((dirs[c[7]], int(c[2:7], 16)) for _,_,c in plan))
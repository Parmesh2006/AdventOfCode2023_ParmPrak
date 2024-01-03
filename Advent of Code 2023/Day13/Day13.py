#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# turn input into a list
ps = list(map(str.split, open('Day13\\input.txt').read().split('\n\n')))

# This function finds out the reflection point numbers
def f(p):
    for i in range(len(p)):
        if sum(c != d for l, m in zip(p[i - 1::-1], p[i:])
                      for c, d in zip(l, m)) == s: 
            return i
    else: 
        return 0

for s in range(0, 2): 
    print(sum(100 * f(p) + f([*zip(*p)]) for p in ps))
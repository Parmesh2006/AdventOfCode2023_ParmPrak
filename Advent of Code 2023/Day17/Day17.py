#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from heapq import heappop, heappush as push

# Keep a complex number coordinate for each of the points in input
G = {i + j * 1j: int(c) for i,r in enumerate(open('Day17\\input.txt'))
                      for j,c in enumerate(r.strip())}

# Using a heap to keep track of the city nodes and to traverse through
def f(min, max, end = [*G][-1], x = 0):
    # Create a todo list
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]

    # A set to add the positions that were seen by the loop as todo was running
    seen = set()

    while todo:
        val, _, pos, dir = heappop(todo)

        if (pos == end): 
            return val
        if (pos, dir) in seen: 
            continue
        
        # add the points seen to "seen"
        seen.add((pos,dir))

        # push the elements from todo into the heap
        for d in 1j / dir, -1j / dir:
            for i in range(min, max + 1):
                if pos + d * i in G:
                    v = sum(G[pos + d * j] for j in range(1, i + 1))
                    push(todo, (val + v, (x := x + 1), pos + d * i, d)) 

# Answer to the first question and second question
print(f(1, 3), f(4, 10))
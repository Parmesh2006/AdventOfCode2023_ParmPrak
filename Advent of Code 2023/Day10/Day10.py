#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Initialize the maze with complex number coordinates
maze = {complex(i, j): c for i, r in enumerate(open('Day10\\input.txt'))
                        for j, c in enumerate(r.strip())}

# Set each pipeline with the direction
N, S, E, W = -1, +1, +1j, -1j
dirs = {'|': (N, S), '-': (E, W), 'L': (N, E),
        'J': (N, W), '7': (S, W), 'F': (S, E),
        'S': (N, E, S, W), '.':()}

# create the graph and start point
graph = {p: {p + d for d in dirs[c]} for p, c in maze.items()}
start = [p for p, d in graph.items() if len(d) == 4][0]

# add all the seen points to seen
seen = {start}
while todo := graph[start]:
    node = todo.pop()
    seen |= {node}
    todo |= graph[node]-seen

irange = lambda n: [complex(n.real, i) for i in range(int(n.imag))]

# Part 1
print(len(seen) // 2)

# Part 2
print(sum(sum(maze[m] in "|JLS" and m in seen for m in irange(p)) % 2
          for p in set(maze) - seen))
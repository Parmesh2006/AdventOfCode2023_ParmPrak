#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

import networkx as nx
from networkx.classes.function import path_weight

# Open the file
with open("Day23\\input.txt") as f:
    ls = f.read().strip().split()

# Track the lengths of the maze components
N, M = len(ls), len(ls[0])
s, t = (0, 1), (N - 1, M - 2)

# Give directions for each
prev = {">": (0, -1), "<": (0, 1), "^": (1, 0), "v": (-1, 0)}
G1 = nx.grid_2d_graph(N, M, create_using=nx.DiGraph)
G2 = nx.grid_2d_graph(N, M)

# Using the grid, remove nodes and edges as it is traversed through
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        p = (i, j)
        if x == "#":
            G1.remove_node(p)
            G2.remove_node(p)
        elif dp := prev.get(x):
            di, dj = dp
            G1.remove_edge(p, (i + di, j + dj))

# Part 1
print(max(map(len, nx.all_simple_edge_paths(G1, s, t))))

# Part 2
# Contract all nodes with exactly two neighbours, keeping track of the
# distance along the way
us = [u for u in G2.nodes if len(G2.edges(u)) == 2]

for u in us:
    v1, v2 = list(G2.neighbors(u))
    new_weight = sum(G2.edges[u, v].get("d", 1) for v in (v1, v2))
    G2.add_edge(v1, v2, d=new_weight)
    G2.remove_node(u)

print(max(path_weight(G2, path, "d") for path in nx.all_simple_paths(G2, s, t)))
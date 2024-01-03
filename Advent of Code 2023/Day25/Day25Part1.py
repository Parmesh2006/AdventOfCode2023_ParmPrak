#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from math import prod
import networkx as nx

# Create a network graph
G = nx.Graph()

# Add the nodes to the network using the input
with open("Day25\\input.txt") as f:
    for line in f:
        v, adj = line.split(": ")
        for a in adj.strip().split(" "):
            G.add_edge(v, a)

# Remove the edges
G.remove_edges_from(nx.minimum_edge_cut(G))

# Find the product of the count of connected components in each group
print(prod([len(c) for c in nx.connected_components(G)]))
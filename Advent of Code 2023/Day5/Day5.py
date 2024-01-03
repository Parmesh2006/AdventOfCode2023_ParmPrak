#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from functools import reduce

# Read the input and separate the seeds
seeds, *mappings = open('Day5\\input.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

# Look up the location number for the seeds
def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src

                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: 
                yield (start, length)
                break

# Prints Part 1 and Part 2
print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])
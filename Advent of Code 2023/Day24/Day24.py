#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

from itertools import combinations
import sympy as sp

# Open File
with open('Day24\\input.txt', 'r') as f:
    puzzle_input = f.read()

# Part One
def part1(puzzle_input, test_input=False):
    # Input all hailstones into the list
    hailstones = []
    for line in puzzle_input.split('\n'):
        nums = line.replace('@', ',').split(',')
        hailstones.append(tuple(map(int, nums)))

    # Test Input, for testing purposes
    if test_input:
        lo, hi = 7, 27
    else:
        lo, hi = 2e14, 4e14
        
    # Counts the total intersections within bounds of all combinations of hailstones
    total = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, dx1, dy1, _ = h1
        x2, y2, _, dx2, dy2, _ = h2
        m1 = dy1 / dx1
        m2 = dy2 / dx2
        
        # they move in parallel and never meet
        if m1 == m2:
            continue

        b1 = y1 - m1 * x1
        b2 = y2 - m2 * x2
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1

        if all((lo <= x <= hi,  # x and y need to be in range
                lo <= y <= hi,
                (x > x1 and dx1 > 0) or (x < x1 and dx1 < 0),  # intersection needs to happen in the future
                (x > x2 and dx2 > 0) or (x < x2 and dx2 < 0))):
            total += 1

    # Return the total count
    return total

# Part Two
def part2(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split('\n')[:3]:
        nums = line.replace('@', ',').split(',')
        first_three_hailstones.append(tuple(map(int, nums)))

    unknowns = sp.symbols('x y z dx dy dz t1 t2 t3')
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t*dx, h[0] + t*h[3]))
        equations.append(sp.Eq(y + t*dy, h[1] + t*h[4]))
        equations.append(sp.Eq(z + t*dz, h[2] + t*h[5]))

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])

# Print part 1 and 2
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
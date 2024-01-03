#! /usr/bin/python3

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""


import re
import sys
from functools import reduce

rule_pat = re.compile(r'([a-z]+)(.)(\d+):(.+)')

# Parses each line with the workflows
def parse_input(path):
    workflows = {}
    parts = []

    for line in open(path).read().strip().split('\n'):
        if ':' in line:
            workflow = {'rules': []}
            workflow['name'], rules_s = line.rstrip('}').split('{')
            rules = []
            for rule_s in rules_s.split(','):
                if ':' in rule_s:
                    key, op, val, target = rule_pat.search(rule_s).groups()
                    workflow['rules'].append(((key, op, int(val)), target))
                else:
                    workflow['rules'].append((None, rule_s))
            workflows[workflow['name']] = workflow
        elif line:
            part = {}
            for word in line.strip('{}\n').split(','):
                k, v = word.split('=')
                part[k] = int(v)
            parts.append(part)
    return workflows, parts

# Invert the workflow to work the other way
def invert(condition):
    key, op, val = condition
    return (key, '>', val - 1) if (op == '<') else (key, '<', val + 1)

# Adds a constraint for the workflow to work with
def add_constraint(constraints, condition):
    key, op, val = condition
    lo, hi = constraints.get(key, (1, 4000))
    if op == '>':
        if val >= hi:
            return None
        lo = val + 1
    else:
        if val <= lo:
            return None
        hi = val - 1
    return dict(constraints, **{key: (lo, hi)})

# Traces the path of the workflow
def trace_paths(workflows, state):
    workflow_name, constraints = state
    for condition, target in workflows[workflow_name]['rules']:
        if condition is None:
            cons_true = constraints
        else:
            cons_true = add_constraint(constraints, condition)
            constraints = add_constraint(constraints, invert(condition))
        if cons_true is not None:
            if target == 'A':
                yield cons_true
            elif target != 'R':
                yield from trace_paths(workflows, (target, cons_true))

# Counts the total paths traced
def count_paths(paths):
    total = 0
    for path in paths:
        total += reduce(int.__mul__, [hi - lo + 1 for lo, hi in path.values()])
    return total

initial_state = ('in', {r: (1, 4000) for r in 'xmas'})

workflows, parts = parse_input("Day19\\input.txt")

print("Part 2:", count_paths(trace_paths(workflows, initial_state)))

#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

timeListMS = 60947882
distListSc = 475213810151650

# For holding the button
lengthFromHolding = []

for time_holding in range(0, timeListMS):
    # initial speed
    initialVelocity = time_holding

    # append the length calculated by the speed * remaining time
    lengthFromHolding.append(time_holding * (timeListMS - time_holding))

# count the number of wins by incrementing every time the length from holding is greater than the record
countOfWins = 0
    
for i in lengthFromHolding:
    if i > distListSc:
        countOfWins += 1

# Print the permutation
print(f"Ways to win: {countOfWins}")
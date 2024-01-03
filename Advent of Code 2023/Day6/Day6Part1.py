#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

inputString = "Time:        60     94     78     82\nDistance:   475   2138   1015   1650"

timeListMS = [int(i) for i in inputString.split("\n")[0].replace("Time:        ", "").split("     ")]
distListSc = [int(i) for i in inputString.split("\n")[1].replace("Distance:   ", "").split("   ")]

# Iterate through all time
waysToWinPermutation = 1

for j in range(0, len(timeListMS)):
    # For holding the button
    lengthFromHolding = []

    for time_holding in range(0, timeListMS[j] + 1):
        # initial speed
        initialVelocity = time_holding

        # append the length calculated by the speed * remaining time
        lengthFromHolding.append(time_holding * (timeListMS[j] - time_holding))

    # count the number of wins by incrementing every time the length from holding is greater than the record
    countOfWins = 0
    
    for i in lengthFromHolding:
        if i > distListSc[j]:
            countOfWins += 1

    # multiply the count of wins to the permutation and the loop will repeat
    waysToWinPermutation *= (countOfWins)

# Print the permutation
print(f"Ways to win: {waysToWinPermutation}")
#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Open file and read all lines
with open(r"Day1\\input.txt") as file:
    lines = [line for line in file]

# sum of calibration values
sumOfCalibrationValues = 0

for line in lines:
    # get all numbers
    allNumbers = []

    for character in line:
        try:
            allNumbers.append(int(character))
        except:
            pass
    
    # Add the numbers to sum of calibration values (a,b) -> a * 10 + b
    sumOfCalibrationValues += (allNumbers[0] * 10 + allNumbers[len(allNumbers) - 1])

print(sumOfCalibrationValues)
#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

import re

# calculates sum between first * 10 and last digit (words included)
def calculate_calibration_value(line):
    # creating possibilities
    possibleNumbersWord = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    possibleNumbersChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(0, 10):
        if possibleNumbersWord[i] in line:
            # replaces zero -> z0o, one -> o1e, two -> t2o
            # preserving first and last letter as buffers because there are overlapping words -> twone, oneight
            line = line.replace(possibleNumbersWord[i], possibleNumbersWord[i][0] + possibleNumbersChar[i] + possibleNumbersWord[i][-1])

    # remove everything that is not a number
    adjustedLine = ""

    for char in line:
        if char in possibleNumbersChar:
            adjustedLine += char

    # Take first digit * 10 and add it to last digit
    return int(adjustedLine[0]) * 10 + int(adjustedLine[-1])

# Open file and read all lines
with open(r"Day1\\input.txt") as file:
   lines = [line for line in file]

# calculate the sum of all calibration values
calibrationValueSum = sum([calculate_calibration_value(line) for line in lines])

# print the calibration values
print(calibrationValueSum)
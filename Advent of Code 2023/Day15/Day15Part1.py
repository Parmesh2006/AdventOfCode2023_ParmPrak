#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

"""
PROCESS:
    1. Determine the ASCII code for the current character of the string.
    2. Increase the current value by the ASCII code you just determined.
    3. Set the current value to itself multiplied by 17.
    4. Set the current value to the remainder of dividing itself by 256.
"""
def HASH_value(string: str) -> int:
    currentValue = 0

    for char in string:
        currentValue += ord(char) # adds the ASCII code of the character
        currentValue *= 17 # set the current value to itself multiplied by 17
        currentValue %= 256 # set the current value to the remainder of that number divided by 256
    
    # the currentValue is the hash value of the string
    return currentValue

# open file and add to list
with open("Day15\\input.txt", "r") as file:
    allCodes = file.read().split(",")

# calculate sum of all hashvalues
sumOfHashVals = 0

for code in allCodes:
    sumOfHashVals += HASH_value(code)

print(sumOfHashVals)
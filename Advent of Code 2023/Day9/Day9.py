#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# GENERATES THE DIFFERENCE SEQUENCE FOR ONE LIST
def differenceSequence(listOfIntegers: list) -> list:
    diffSeq: list = []

    for i in range(0, len(listOfIntegers) - 1):
        diffSeq.append(listOfIntegers[i + 1] - listOfIntegers[i])

    return diffSeq

# CHECKS IF ALL ELEMENTS ARE EQUAL
def allEqualElements(listOfIntegers: list) -> list:
    for i in range(0, len(listOfIntegers) - 1):
        if listOfIntegers[i] != listOfIntegers[i + 1]:
            return False
    
    return True

# GENERATES THE DIFFERENCE SEQUENCES FROM THE ORIGINAL SEQUENCE
def getAllDifferenceLists(listOfIntSeq: list) -> list:
    differenceLists: list = []
    differenceLists.append(listOfIntSeq)

    listOfDiffs: list = differenceSequence(listOfIntSeq)

    while (not allEqualElements(listOfDiffs)):
        differenceLists.append(listOfDiffs)

        listOfDiffs = differenceSequence(listOfDiffs)
    
    differenceLists.append(listOfDiffs)

    return differenceLists

"""
PART 1: FINDING THE NEXT TERM TO THE RIGHT
"""
def nextTerm(listOfIntSeq: list) -> int:
    differencesLists: list = getAllDifferenceLists(listOfIntSeq)

    # The next term is the sum of all of the last elements
    sumOfElems: int = 0

    for diffList in differencesLists:
        sumOfElems += diffList[-1]

    # return the sum
    return sumOfElems

"""
PART 2: FINDING THE PREVIOUS TERM TO THE LEFT
"""

# Open file and extract information
with open("Day9\\input.txt") as file:
    lines = [line.replace("\n", "") for line in file]

sumOfNextTerms = 0
sumOfPrevTerms = 0

for line in lines:
    listOfIntSeq: list = [int(i) for i in line.split(" ")]

    sumOfNextTerms += nextTerm(listOfIntSeq)
    sumOfPrevTerms += nextTerm(listOfIntSeq[::-1])

"""
OUTPUT
"""

print(sumOfNextTerms)
print(sumOfPrevTerms)
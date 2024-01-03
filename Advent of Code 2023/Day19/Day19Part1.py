#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# adds the input item to dictionary
def addToConditionDictionary(dictionary: dict, item: str) -> dict:
    key = item[0:item.index("{")]
    value = item[item.index("{") + 1 : item.index("}")]
    valueSplitted = value.split(",")
    
    valuesFullySplitted = []
    for i in valueSplitted:
        if ":" in i:
            item = i.split(":")
            
            valuesFullySplitted.append(item)
        else:
            valuesFullySplitted.append(i)
                
    dictionary[key] = valuesFullySplitted

def addTestValuesToList(listToAddTo: list, testValue: str) -> list:
    # test values: {a=1,b=2,c=3,d=4}
    listToAddTo.append(
        testValue.replace("{", "").replace("}", "").split(",") if "\n" not in testValue else
        testValue.replace("{", "").replace("}", "").replace("\n", "").split(",")
        )

# Open file and preprocess
dictionaryOfConditions: dict = dict()
testValuesList: list = []

with open("Day19\\input.txt") as file:
    for line in file:
        if line[0] != "{":
            if line != "\n":
                addToConditionDictionary(dictionaryOfConditions, line)
        else:
            addTestValuesToList(testValuesList, line)

# Keep track of passed test values
passedTestValues = []

# Go through each test value
for testValue in testValuesList:
    # Join all the variables into one string
    testValueVariablesJoined: str = ";".join(testValue)

    # compile and execute the variable assignment
    execCode = compile(testValueVariablesJoined, 'filename', 'exec')
    exec(execCode)

    # currentPart: calculated, but all parts start at "in"
    currentPart = "in"
    
    while currentPart not in ["A", "R"]:
        conditionList = dictionaryOfConditions[currentPart]

        for condPair in conditionList:
            if type(condPair) == list:
                # length of condition is always 2
                condition = condPair[0]
                toDo = condPair[1]

                srcCode = f"condValue = {condition}"
                execCode = compile(srcCode, 'filename', 'exec')
                exec(execCode)

                # condValue is defined by srcCode
                if condValue:
                    currentPart = toDo
                    break
                else:
                    continue
            else:
                currentPart = condPair

    if currentPart == "A":
        passedTestValues.append(testValue)

# Take all the passed values and calculate xmas rating for each
sumOfXMASRatings = 0

for xmas in passedTestValues:
    srcCode = ';'.join(xmas)

    # compile and run the assignment
    execCode = compile(srcCode, 'filename', 'exec')
    exec(execCode)

    # add the xmas values to the sum
    sumOfXMASRatings += (x + m + a + s)

# Print the sum
print(sumOfXMASRatings)
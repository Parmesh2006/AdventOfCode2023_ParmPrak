#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Checks if row is empty
def isRowEmpty(galaxyRow: list) -> bool:
    for i in galaxyRow:
        if i != ".":
            return False
    
    return True

# Checks if column is empty
def isColumnEmpty(galaxyMap: list[list], colIndex: int) -> bool:
    for i in range(0, len(galaxyMap)):
        if galaxyMap[i][colIndex] != ".":
            return False
    
    return True

# Doubles every empty column and every empty row
def expandMap(galaxyMap: list[list]) -> list:
    # expand every empty row
    newGalaxyMap: list[list] = []

    for row in galaxyMap:
        if isRowEmpty(row):
            newGalaxyMap.append(row)
            newGalaxyMap.append(row)
        else:
            newGalaxyMap.append(row)

    # expand every empty column
    editedGalaxyMap: list[list] = []

    for row in newGalaxyMap:
        newRow: list = []

        for i in range(0, len(row)):
            if isColumnEmpty(newGalaxyMap, i):
                newRow.append(row[i])
                newRow.append(row[i])
            else:
                newRow.append(row[i])
        
        editedGalaxyMap.append(newRow)

    return editedGalaxyMap

# Stores coordinates of all galaxies in a list and returns that list
def coordinatesOfAllGalaxiesInList(galaxyMap: list[list]) -> list:
    listOfCoordinates: list = []

    for row in range(0, len(galaxyMap)):
        for col in range(0, len(galaxyMap[row])):
            if galaxyMap[row][col] == "#":
                # tuple (row, col) is appended
                listOfCoordinates.append((row, col))
    
    return listOfCoordinates

# Finds the distance between each combination of coordinates
def findTotalDistance(coordinatesMap: list) -> int:
    totalDistanceList = []

    for i in range(0, len(coordinatesMap) - 1):
        for j in range(i + 1, len(coordinatesMap)):
            # find distance between coordinatesMap[i] and coordinatesMap[j]

            coor1 = coordinatesMap[i]
            coor2 = coordinatesMap[j]

            distance = abs(int(coor2[0]) - int(coor1[0])) + abs(int(coor2[1]) - int(coor1[1]))
            
            # add distance to total distance
            totalDistanceList.append(distance)

    # return total 
    return sum(totalDistanceList)

# Open file and read
gmList = []

with open("Day11\\input.txt") as file:
    for line in file:
        newSplitLines = []

        for char in line:
            if char != "\n":
                newSplitLines.append(char)

        gmList.append(newSplitLines)

# Preprocess list
newGmList = []
temp = []
for i in gmList:
    for j in i:
        temp.append(j)

    newGmList.append(temp)
    temp = []

# Expand the map
expandedGalaxyMap = expandMap(newGmList)

# Get Coordinates
coordinates = coordinatesOfAllGalaxiesInList(expandedGalaxyMap)

# Find the total distance (PART 1)
print(findTotalDistance(coordinates))

# Find the total distance (PART 2)
print(findTotalDistance(coordinates) + 512232 * 999998)
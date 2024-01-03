#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Find Product of Minimum Red, Minimum Green, and Minimum Blue
def productMinRGB(gameString: str) -> int:
    numberOfRed: list = []
    numberOfBlue: list = []
    numberOfGreen: list = []

    # Just get the colors and numbers in each game
    games: list = gameString.split(": ")[1].split("; ")

    # Iterate through games
    for game in games:
        colors: list = game.split(", ")

        for color in colors:
            if "red" in color:
                numberOfRed.append(int(color.replace(" red", "")))
            elif "blue" in color:
                numberOfBlue.append(int(color.replace(" blue", "")))
            elif "green" in color:
                numberOfGreen.append(int(color.replace(" green", "")))

    # Multiply out the maximums of each list and return the product
    return max(numberOfBlue) * max(numberOfGreen) * max(numberOfRed)

# Open file and read all lines
with open(r"Day2\\input.txt") as file:
   lines = [line for line in file]

# Find the sum of the valid game numbers in the file
sumOfProductsMinRGB = sum([productMinRGB(game) for game in lines])

# Print out result
print(sumOfProductsMinRGB)
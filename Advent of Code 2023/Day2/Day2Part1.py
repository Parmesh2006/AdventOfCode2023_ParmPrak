#!/usr/bin/python

"""
THIS IS THE CORRECT SOLUTION.

AUTHOR: Parmeshvar Prakash
"""

# Validate Game Method
def validateGame(gameString: str) -> int:
    # split between colon
    splitBetGameAndColors: list = gameString.split(": ")

    # get game number
    gameNumber: int = int(splitBetGameAndColors[0].replace("Game ", ""))

    # split between games by "; "
    allGames = splitBetGameAndColors[1].split("; ")

    # iterate through all games and count up total colors
    validGames = []

    for game in allGames:
        splitGameByComma = game.split(", ")
        blueInGame: int = 0
        redInGame: int = 0
        greenInGame: int = 0

        for color in splitGameByComma:
            if "blue" in color:
                blueInGame = int(color.replace(" blue", ""))
            elif "red" in color:
                redInGame = int(color.replace(" red", ""))
            elif "green" in color:
                greenInGame = int(color.replace(" green", ""))

        # Check if in game counts are less than or equal to restraints
        if redInGame <= 12 and greenInGame <= 13 and blueInGame <= 14:
            validGames.append(True)
        else:
            validGames.append(False)
            break        

    # Validate the game: if it is valid, return the game number, or else return 0
    if False in validGames:
        return 0
    else:
        return gameNumber
    
# Open file and read all lines
with open(r"Day2\\input.txt") as file:
   lines = [line for line in file]

# Find the sum of the valid game numbers in the file
sumOfGameNumbers = sum([validateGame(game) for game in lines])

# Print out result
print(sumOfGameNumbers)
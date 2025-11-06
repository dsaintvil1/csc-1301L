"""
Danerick Saint-Vil
October 30, 2025
Program 1
scrabble.py
"""
# Dictionary of letters and the amount of points per letter
letter_points = {
    "A":1,"B":3,"C":3, "D":2, "E":1, "F":4, "G":2,
    "H":4, "I":1, "J":8, "K":5, "L":1, "M":3, "N": 1, "O":1, "P":3,
    "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, 
    "W":4, "X":8, "Y":4, "Z":10
}

# Takes an input and capitalizes every letter
word = input(":> ").upper()

while word not in ["QUIT", "Q"]: # If the input is "quit" or "q", the code ends
    points = 0 # Resets the point value to 0
    for x in word: # For every letter in the variable word
        points += letter_points[x] # Adds the point value from the dictionary to the points variable
    print(f"{word} is worth {points} points.")
    word = input(":> ").upper() # Resets the word variable to the next input
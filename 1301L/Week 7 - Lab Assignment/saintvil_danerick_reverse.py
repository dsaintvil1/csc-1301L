"""
Danerick Saint-Vil
October 9, 2025
Program 2
reverse.py

"""
# Loops forever (edit: use true for simpler code)
while True:

    # Gets the original string
    string = input("Please Enter Your String: ")

    # Checks to see if quit was inputted
    if string == "Quit" or string == "quit" or string == "q":
        quit()

    # Sets reverse as an empty string
    reverse = ""

    # For every letter of reversed(string) (We learned that way to reverse in class, but the instructions ask for range)
    for x in range(len(string)-1, -1, -1):
       reverse += string[x] # Adds the letters in reverse order

    print(f"Reversed: {reverse}")
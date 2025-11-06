"""
Danerick Saint-Vil
September 4, 2025
Variables and Expressions: Project 1

"""

name = input("Please enter your name: ") # Asks for your name
day = input("What day of the week is your lab on: ") # Asks for the day of the week of the lab
time = input("At what time is your lab: ") # Ask what time your lab is

print("Hello ", name, "!", sep="") # Prints "Hello [name]!" using your input of your name
print("Welcome to the CSC 1301 Lab Course!")
print("Our lab session is held every ", day, " at ", time, ".", sep="") # Uses the input of the day and time to say when class is held
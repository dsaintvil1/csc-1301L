"""
Danerick Saint-Vil
September 11, 2025
Basic Data Types: Program 3
modules.py

"""
import math # Imports the math module
import random # Imports the random module

r = int(input("Please enter the radius of the sphere: ")) # Gets the radius of the sphere

vol = (4 / 3) * math.pi * math.pow(r, 3) # Calculates the volume of the sphere

print(f"The volume of a sphere with raduis of {r} is {vol:.2f}")

rand_num = random.randint(1, 10) # Gets a random integer between 1 and 10

factorial = math.factorial(rand_num) # Gets the factorial of that number

print(f"The factorial of {rand_num} is {factorial}") 

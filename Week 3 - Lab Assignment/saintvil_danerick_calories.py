"""
Danerick Saint-Vil
September 11, 2025
Basic Data Types: Program 1
calories.py

"""
age = float(input("Please enter your age: ")) # Gets your age
weight = float(input("Please enter your weight in pounds: ")) # Gets your weight in pounds
h_rate = float(input("Please enter your heart rate in beats per minute: ")) # Gets heart rate in bpm
time = float(input("Please enter the length of your workout in minutes: ")) # Gets your workout length

calories = ((age * 0.2757 + weight * 0.03295 + h_rate * 1.0781 - 75.4991) * time) / 8.368
# Calculates the amount of calories burnt

print(f"Calories burned: {calories:.2f}") # Prints the amount of calories burnt




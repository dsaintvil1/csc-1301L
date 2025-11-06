"""
Danerick Saint-Vil
October 9, 2025
Program 3
normalize.py

"""
# List for Floating-Point Values and Normalized Floating-Point Values
FPV = []
NFPV = []

# Gets the amount of repetitions desired
repetitions = int(input("Please enter the number of floating-point values: "))

# Loops for the amount specified
for x in range(repetitions):
    # Gets a floating-point value
    FPV.append(float(input("Please enter a floating-point value: ")))

# Loops for each value in FPV
for x in FPV:
    NFPV.append(x / max(FPV)) # Adds the normalized number to the list

print("\nNormalized Floating-Point Values: ")

# Prints every value in NFPV
for x in NFPV:
    print(f"{x:.2f}")
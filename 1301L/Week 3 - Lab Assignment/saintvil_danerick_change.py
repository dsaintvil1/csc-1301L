"""
Danerick Saint-Vil
September 11, 2025
Basic Data Types: Program 2
change.py

"""
cents = int(input("Please enter a number of cents: ")) # Gets number of cents

q = cents // 25 # Gets the amount of quarters

d = (cents % 25) // 10 # Gets the amount of dimes

n = ((cents % 25) % 10) // 5 # Gets the amount of nickels

p = (((cents % 25) % 10) % 5) # Gets the amount of pennies

if q == 1:
    qu = "quarter"
else:
    qu = "quarters"
if d == 1:
    di = "dime"
else:
    di = "dimes"
if n == 1:
    ni = "nickel"
else:
    ni = "nickels"
if p == 1:
    pe = "penny"
else:
    pe = "pennies"
# All these if else statements hange grammar depending on the number. If the number is one, the word will be singular.

print(f"Coins: {q} {qu}, {d} {di}, {n} {ni}, {p} {pe}")
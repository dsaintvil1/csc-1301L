"""
Danerick Saint-Vil
September 25, 2025
Program 1
speeding.py

"""
# Gets the speed limit
speed_lim = int(input("Please enter the speed limit for the road: "))
# Gets the speed of the car
speed_car = int(input("Please enter the vehicle's recorded speed: "))

# Puts the fines in a list
fines = ["$50", "$75", "$150", "$300", "There is no fine."]

if speed_car <= speed_lim - 10: # Checking to see if you are driving 10 or more mph below the speed limit
    print(f"The speeding fine is {fines[0]}")
elif speed_car >= speed_lim + 6 and speed_car <= speed_lim + 20: # Checking to see if you are driving 6-20 mph above the speed limit
    print(f"The speeding fine is {fines[1]}")
elif speed_car >= speed_lim + 21 and speed_car <= speed_lim + 40: # Checking to see if you are driving 21-40 mph above the speed limit
    print(f"The speeding fine is {fines[2]}")
elif speed_car > speed_lim + 40: # Checking to see if you are driving above 40 mph
    print(f"The speeding fine is {fines[3]}")
else: # If the other things aren't true, you won't be fined
    print(fines[4])

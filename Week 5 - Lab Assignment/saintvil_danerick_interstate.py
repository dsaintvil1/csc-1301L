"""
Danerick Saint-Vil
September 25, 2025
Program 2
interstate.py

"""

# Gets the interstate number
interstate = int(input("Please enter an interstate number: "))




if interstate > 0 and interstate < 100: # If the input is between 1-99 (primary interstate)
    print(f"I-{interstate} is primary, ", end = "")
    if interstate % 2 == 1: # Checks for odd number
        print("going north/south.")

    else: # If not odd, assume it's even
        print("going east/west") 

elif interstate > 99 and interstate < 1000: # If the input is between 100-999 (auxilary interstate)
    prime = interstate % 100 # Prime is the primary highway this auxilary highway connects to

    if prime <= 0: # If prime is not a valid primary highway number
        print(f"{interstate} is not a valid interstate highway number.")
        quit() # Ends the code
    
    print(f"I-{interstate} is auxilary, serving I-{prime}, ", end = "")
    if prime % 2 == 1: # Checks for odd number
        print("going north/south.")

    else: # If not odd, assume it's even
        print("going east/west") # See above (function)

else: # If the number is not between 1-999, it is not valid
    print(f"{interstate} is not a valid interstate highway number.")
    quit() # Ends the code

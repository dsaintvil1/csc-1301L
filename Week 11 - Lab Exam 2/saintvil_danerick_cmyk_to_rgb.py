"""
Danerick Saint-Vil
November 6, 2025
Lab Exam 2
cmyk_to_rgb.py
"""
def range_error(): # This function will display that a range error has occured
    print("Error: Value must be between 0 and 100.")

def CMYK_to_RGB(cmyk): # This function converts cmyk to rgb using an input of the dictionary
    rgb = dict() # Creates (or empties) an rgb dictionary
    
    # Adds a digit to the dictionary using the equation (The floor division is in order to round it)
    rgb["R"] = (255 * (1 - (cmyk['C'] / 100)) * (1 - (cmyk['K'] / 100))) // 1
    rgb["G"] = (255 * (1 - (cmyk['M'] / 100)) * (1 - (cmyk['K'] / 100))) // 1
    rgb["B"] = (255 * (1 - (cmyk['Y'] / 100)) * (1 - (cmyk['K'] / 100))) // 1

    return rgb
# The YN variable determines whether or not you want to continue the loop
YN = ''


while YN != "no": # Loops until the YN variable is 'no'
    print("\nCMYK To RGB Converter")
    print("---------------------------")

    CMYK = dict() # Creates (or empties) a CMYK dictionary
    RGB = dict() # Creates (or empties) an RGB dictionary

    # First, gets an input for the specified color
        # color = int(input("Enter the {color} Color Value"))
    # Initiates a loop while the color's value is outside the range (0-100)
        # while color < 0 or color > 100:
            # Use the range_error function
            # Ask for the input again
    C = int(input("Enter The Cyan Color Value: ")) # Cyan
    while C < 0 or C > 100:
        range_error()
        C = int(input("Enter The Cyan Color Value: "))

    M = int(input("Enter The Magenta Color Value: ")) # Magenta
    while M < 0 or M > 100:
        range_error()
        M = int(input("Enter The Magenta Color Value: "))

    Y = int(input("Enter The Yellow Color Value: ")) # Yellow
    while Y < 0 or Y > 100:
        range_error()
        Y = int(input("Enter The Yellow Color Value: "))

    K = int(input("Enter The Key Color Value: ")) # Key (Black)
    while K < 0 or K > 100:
        range_error()
        K = int(input("Enter The Key Color Value: "))
    
    print("\n")
    # Next, store these values in a dictionary
    CMYK['C'] = C
    CMYK['M'] = M
    CMYK['Y'] = Y
    CMYK['K'] = K

    # Set RGB to a caluculated dictionary (using a function)
    RGB = CMYK_to_RGB(CMYK)

    # Print the RGB Values
    print("RGB Values")
    print(f"Red: {int(RGB["R"])}")
    print(f"Green: {int(RGB["G"])}")
    print(f"Blue: {int(RGB["B"])}")

    print("---------------------------")

    # Ask if you want to do it again
    YN = input("Would you like to perform another conversion? (yes/no): ").lower()

else: # If YN is 'no', end the loop
    print("Goodbye!")
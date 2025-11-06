"""
Danerick Saint-Vil
October 16, 2025
Program 2
steps.py

"""
# Create a function to convert from feet to steps
def feet_to_steps(f): # local var f is meant to represent feet
    return f / 2.5 # Returns the amount of steps

def main():
    # Gets your input for number of feet
    feet = float(input("Please enter the distance travelled in feet: "))

    print(f"{int(feet_to_steps(feet))} steps") # Prints the amount of steps as an integer

main()
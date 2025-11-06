"""
Danerick Saint-Vil
October 9, 2025
Program 1
password.py

"""
# Gets the password
password = input("Please Enter Your Password: ")

# Variable for adding each letter of password
strengthened = ""

# Checks every letter of the password, and adds it to the new string
for key in password:
    # If the letter is one of the following, replaces it with another digit/letter/symbol
    if key == "o":
        strengthened += "0"
    elif key == "i":
        strengthened += "1"
    elif key == "a":
        strengthened += "@"
    elif key == "e":
        strengthened += "3"
    elif key == "A":
        strengthened += "4"
    elif key == "B":
        strengthened += "8"
    elif key == "s":
        strengthened += "$"
    else: # Else add the original letter
        strengthened += key
        
# Appends an exclamation point to the end
strengthened += "!"

print(f"Your new strong password is: {strengthened}")
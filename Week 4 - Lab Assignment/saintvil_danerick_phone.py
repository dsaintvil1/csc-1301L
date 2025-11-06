"""
Danerick Saint-Vil
September 18, 2025
Program 1
phone.py

"""
# Get the input of the phone number
phone_num = int(input("Please enter your phone number: "))

# Gets the first three numbers
first3 = phone_num // 10000000

# Gets the middle three numbers
middle3 = (phone_num % 10000000) // 10000

# Gets the last three numbers
last3 = phone_num % 10000

# Prints the edited number
print(f"Phone Number: ({first3}) {middle3}-{last3}")
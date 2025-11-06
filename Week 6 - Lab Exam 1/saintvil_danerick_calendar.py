"""
Danerick Saint-Vil
October 2, 2025
Exam 1 - Programming Lab
calendar.py

"""
# List of months to check spelling
month_list = ["January", 
              "February", 
              "March", 
              "April", 
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]

# List of months with 30 days
thirty = ["April", "June", "September", "November"]

# List of months with 31 days
thirty_one = ["January", "March", "May", "July", "August", "October", "December"]

# Input to get the month (automatically a string)
month = input('Please enter the month: ')

# Input to get the day
day = int(input('Please enter the day: '))

# Checks to see if the month input is valid
if month not in month_list:
    print(f"Invalid Input: {month} is not a valid month!")
    quit() # Ends the code (I dont want all my main code in an "else" bracket)

# Checks to see if the day input is valid
if day == 0: # If the day is zero
    print(f"Invalid Input: Date ({day}) can not be zero!")
    quit()
elif day < 0: # If the day is negative
    print(f"Invalid Input: Date ({day}) can not be negative!")
    quit()
elif month == "February" and day > 28: # If the month is suppossed to have 28 days but has more
    print(f"Invalid Input: There is no {day} of {month}!")
    quit()
elif month in thirty and day > 30:# If the month is suppossed to have 30 days but has more
    print(f"Invalid Input: There is no {day} of {month}!")
    quit()
elif month in thirty_one and day > 31: # If the month is suppossed to have 31 days but has more
    print(f"Invalid Input: There is no {day} of {month}!")
    quit()

# Now the main line of code can begin (For the following dates, everything is inclusive)

# First, checks the dates in the range of January 12 - May 5
if (month in ["February", "March", "April"]) or (month == "January" and day >= 12) or (month == "May" and day <= 5):
    print(f"{month} {day} is during GSU's spring semester.")
# Next, checks the dates in the range of May 6 - August 24
elif (month in ["June", "July", "August"]) or (month == "May" and day >= 6) or (month == "August" and day <= 24):
    print(f"{month} {day} is during GSU's summer break.")
# Then, checks the dates in the range of August 25 - December 16
elif (month in ["September", "October", "November"]) or (month == "August" and day >= 25) or (month == "December" and day <= 16):
    print(f"{month} {day} is during GSU's fall semester.")
# Else, assume the date lies between December 17 - January 11
else:
    print(f"{month} {day} is during GSU's winter break.")
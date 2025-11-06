"""
Danerick Saint-Vil
September 18, 2025
Program 2
grades.py

"""

# Sets of class attendees for the first and second days
day1 = {'William', 'Daphne', 'Erika', 'Adam', 'Percy', 'Brock', 'Jessica', 'Trent', 'Mahmoud'}
day2 = {'Daphne', 'Alex', 'Percy', 'Mahmoud', 'Jessica', 'Adam', 'Trent', 'Caleb', 'Zayne', 'Erika'}

# Gets the people who attended both days
attend_2days = set(day1 & (day2))
# Gets the people who attended one days
attend_1day = set(day1.symmetric_difference(day2))
# Gets the total number of students
num_students = len(day1.union(day2))

# Prints info (self explanatory)
print(num_students, "students attended the class.")
print(attend_2days, "attended both class days.")
print(attend_1day, "attended one class day.")
# \n is to match the example terminal given
print("\n")

# Set of grades
grades = [88, 96, 96, 76, 89, 74, 100, 85, 75, 77, 100, 98]

# Gets the highest grade
high = max(grades)
# Gets the lowest grade
low = min(grades)
# Gets the average of all the grades
avg = sum(grades) / len(grades)

# Prints info (self explanatory)
print(f"The highest grade was a {high}")
print(f"The lowest grade was a {low}")
print(f"The average grade for the exam was a {avg:.1f}")


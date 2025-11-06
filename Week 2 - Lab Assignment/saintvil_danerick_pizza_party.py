"""
Danerick Saint-Vil
September 4, 2025
Variables and Expressions: Project 3

"""
num_ppl = int(input("Please enter the number of people attending the party: ")) # Gets the number of people at the party
num_pizza = int(input("Please enter the number of pizzas purchased for the party: ")) # Gets the number of pizzas ordered
d = int(input("Please enter the diameter of the pizzas: ")) # Gets the diameter of each pizza
num_slices = int(input("Please enter the number of slices per pizza: ")) # Gets the number of slices of each pizza

r = d / 2 # Gets the radius

t_area = float((3.14 * r * r) * num_pizza) # Calculates the area of all pizzas together
area_per = float(t_area / num_ppl) # Calculates area per person
t_slices = int(num_pizza * num_slices) # Calculates number of slices of all pizzas together
slices_per = float(t_slices / num_ppl) # Calculates the number of slices per person

print("Total pizza area:", t_area, "square inches")
print("Total number of slices:", t_slices)
print("Pizza area per person:", area_per, "square inches")
print("Slices per person:", slices_per)
"""
Danerick Saint-Vil
September 18, 2025
Program 3
food.py

"""
# Dictionary of foods with prices
menu = {
    'Hot Dog' : 1.50,
    'Slice of Pizza' : 1.99,
    'Whole Pizza' : 9.95,
    'Chicken Bake' : 3.99,
    'Soft Drink' : 0.69,
    'Ice Cream Sundae' : 2.49
}

# Prints menu
print(menu)

# Gets the number of each item you want, multiplies it to the price of the item, then adds it to the total price
price = int(input('Please enter the number of Hot Dogs: ')) * menu['Hot Dog']
price += int(input('Please enter the number of Pizza Slices: ')) * menu['Slice of Pizza']
price += int(input('Please enter the number of Whole Pizzas: ')) * menu['Whole Pizza']
price += int(input('Please enter the number of Chicken Bakes: ')) * menu['Chicken Bake']
price += int(input('Please enter the number of Soft Drinks: ')) * menu['Soft Drink']
price += int(input('Please enter the number of Ice Cream Sundaes: ')) * menu['Ice Cream Sundae']

# Prints the total price
print(f"The total cost of the order is ${price}")
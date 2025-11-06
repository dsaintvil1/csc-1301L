"""
Danerick Saint-Vil
October 16, 2025
Program 3
text_filter.py

"""
# List of banned words
banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]

def text_filter(str): # This function filters out the words from the banned list
    new = "" # This is where the new string will be
    split_str = str.split() # Turns the inputted string into a list
    for x in split_str: # For every word in your input...
        if x in banned_words: # If your word is in the list of banned words
            split_str.remove(x) # Removes the word from your input
    for x in split_str: # For every word in your new output (which is currently a list)...
        new += f"{x} " # Adds each word to the new string
    return new # Returns the output

def main():
    input_string = input(">: ") # Gets your inputted string

    print(f"Input Message: {input}") # Prints your original string
    print(f"Output Message: {text_filter(input_string)}") # Prints the new string

main()




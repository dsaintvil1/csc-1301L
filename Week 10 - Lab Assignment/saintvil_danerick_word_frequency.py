"""
Danerick Saint-Vil
October 30, 2025
Program 2
word_frequency.py
"""

# Creates an empty dictionary
bag_of_words = {}

# Builds a dictionary with (key = the words in a list) and (value = the amount of iterations of the word)
def build_dictionary(wordList):
    for x in wordList: # For each word
        bag_of_words[x] = 0 # Adds them to the dictionary with a value of 0
    for x in wordList:
        bag_of_words[x] += 1 # Goes back and adds 1 for every iteration of a word

input_str = input(":> ").lower() # Gets the input and makes it all lowercase

input_list = input_str.split() # Splits the string into a list

print(f"\nWord List:\n{input_list}\n") # Prints the list of words

input_list.sort() # Sorts the list in alphabetical order

build_dictionary(input_list) # See lines 11-16

print("Bag of Words:")

for word, iterations in bag_of_words.items(): # For each key and value in the dictionary
    print(f"{word} - {iterations}") # Prints the key and value


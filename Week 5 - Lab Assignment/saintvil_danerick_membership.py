"""
Danerick Saint-Vil
September 25, 2025
Program 3
membership.py

"""
# List of vowels, digits, and punctuation
vowels = ['a', 'e', 'i', 'o', 'u']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = [',', ';', '.', '?', '!']

while i:=1: # Forever loop (to facilitate running the code several times)
    character = input("Please enter a character: ") # Gets your inputted character

    #in these next if statements, 'identity' is what the character is

    if character in vowels: # Searches vowels list
        identity = 'vowel'
    elif character in digits: # Searches digits list
        identity = 'digit'
    elif character in punctuation: # Searches punctuation list
        identity = 'punctuation'
    else: # Assumes your character is a consonant
        identity = 'consonant'

    print(f"The character '{character}' is a {identity}", "\n") # Added a \n to facilitate the looping

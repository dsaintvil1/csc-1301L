"""
Danerick Saint-Vil
October 16, 2025
Program 1
guess_my_number.py

"""
# Get the random module
import random

# Gets a random number
answer = random.randint(1,100)

print("I have generated a random number between 1 and 100. You will have 10 attempts to guess that number.")


for x in range(10): # For 10 iterations...
    
    # Gets the input f your guess (the x+1 displays what turn ur on)
    guess = int(input(f"Guess {x+1}: "))

    if guess == answer: # If you guessed correctly...
        print("You correctly guessed my random number!")
        break # Ends the loop

    elif guess > answer: # If your guess was greater than the number...
        print("Your guess is greater than my random number. Try Again.")

    elif guess < answer:# If your guess was less than the number...
        print("Your guess is less than my random number. Try Again.")
else:
    print("You have run out of attempts.")

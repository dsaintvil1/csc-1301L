from gtts import gTTS
import os

name = input("Please enter your name: ") # Asks for your name
day = input("What day of the week is your lab on: ") # Asks for the day of the week of the lab
time = input("At what time is your lab: ") # Ask what time your lab is

message = f"Hello {name}! Welcome to the CSC 1301 Lab Course! Our lab session is held every {day} at {time}."

tts = gTTS(text= message, lang='en')
tts.save("welcome.mp3")

os.system("start welcome.mp3")
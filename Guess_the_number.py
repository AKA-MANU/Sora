
"""
Create a game where the computer generates a random number,
and the player guesses it. 
Provide hints (higher/lower) after each guess
Skills: Basic input/output, conditionals (if statements), loops
(while), random module.
Why: Teaches core programming logic and user interaction.
"""

import random as rd
import time

final_number = rd.randint(1,50)
print("Welcome to my guessing game")
time.sleep(1)
print("Guessing number is betwween 1 to 50")
time.sleep(1)
print("Good luck!")

print("Choose the difficulty level: Easy / Medium / Hard")
Difficulty = input("Enter the difficulty").lower()

if Difficulty == "easy":
    max_attempts = 10
elif Difficulty == "medium":
    max_attempts = 6
elif Difficulty == "hard":
    max_attempts = 3
else:
    print("Invalid input setting difficulty to easy")
    max_attemps = 8

attempts = 0
guess = None
while guess != final_number and attempts < max_attempts:
     
    guess = int(input("Enter your guess"))
    attempts += 1
    
    if guess < final_number:
        print("\nHigher")
    elif guess > final_number:
        print("\nLower")
    else:
        print(f"Congracts! you guess the correct number in {attemps} attemps, Well_done!." )
    
if final_number != max_attempts:
    print(f"You are noob, go play ludo {attempts} attempts  final_number is {final_number}")    







#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def random_number():
    """Generates a random number between 1 and 100
    using random, and then returns that number."""
    
    return random.randint(0,100)

def get_difficulty():
    """Based on a dictionary of difficulties and users input, 
    a number of lives is returned."""
    
    difficulties = {
        "easy": 10,
        "medium": 5,
        "impossible": 1,
    }

    selected_difficulty = input("Choose a Difficulty: Easy, Medium, impossible: ").lower()

    for difficulty in difficulties:
        if selected_difficulty == difficulty:
            print(f"You have selected {difficulty}.")
            return difficulties[difficulty]
    print("Invalid Input: 1 LIFE ONLY. Sorry ;)")
    return difficulties["impossible"]

def higher_or_lower(guessing_number, actual_number):
    """Takes two numbers, the first is the guess, and
    the second is the correct number. Based on this info it
    tells the user if their next guess should be higher or lower"""
    
    if guessing_number > actual_number:
        print("Lower.")
    else:
        print("Higher.")

def start_game(number_of_lives, correct_number):
    """Takes the chosen lives and generated number, 
    then proceeds to run the main loop of the guessing game."""
    
    round_over = False
    while not round_over:
        print(f"You have {number_of_lives} live(s) left.")
        guess = int(input("Guess a number: "))

        if guess == correct_number:
            print("You win!")
            round_over = True
        else:
            number_of_lives -= 1

            if number_of_lives == 0:
                print(f"Game over, the number was {correct_number}.")
                round_over = True
            else:
                higher_or_lower(guess, correct_number)

print(logo)
game_is_over = False
while not game_is_over:
    print("Welcome to Guess The Number!")
    print("I'm guessing of a number between 1 and 100.")
    
    lives = get_difficulty()
    number = random_number()

    start_game(lives, number)

    again = input("Do you want to play again? y/n: ").lower()

    if again != "y":
        game_is_over = True

    
    

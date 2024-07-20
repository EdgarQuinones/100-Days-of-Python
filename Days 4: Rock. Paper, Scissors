rock_image = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_image = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_image = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rock = "0"
paper = "1"
scissors = "2"

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
bot_choice = str(random.randint(0,2))

if user_choice == rock:
    print(rock_image)
elif user_choice == paper:
    print(paper_image)
elif user_choice == scissors:
    print(scissors_image)
else:
    print("Invalid Entry, Exiting.")
    exit()

print("Computer chose: ")

if bot_choice == rock:
    print(rock_image)
elif bot_choice == paper:
    print(paper_image)
elif bot_choice == scissors:
    print(scissors_image)

if user_choice == bot_choice:
    print("Draw\n-")
elif user_choice == rock:
    if bot_choice == paper:
        print("You lose")
    else:
        print("You win!")
elif user_choice == paper:
    if bot_choice == scissors:
        print("You lose")
    else:
        print("You win!")
else: #User entered Scissors
    if bot_choice == rock:
        print("You lose")
    else:
        print("You win!")

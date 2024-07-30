import random

from replit import clear

import art
from game_data import data


def get_topic(instagram_accounts):
    random_number = random.randint(0, len(instagram_accounts) - 1)
    new_topic = instagram_accounts[random_number]
    return new_topic

def start_game(topic_a, topic_b):
    topic_a_followers = topic_a['follower_count']
    topic_b_followers = topic_b['follower_count']
    correct_letter = 'A' if topic_a_followers > topic_b_followers else 'B'
    
    print(f"Compare A: {display_topic(topic_a)}")
    print(art.vs)
    print(f"Against B: {display_topic(topic_b)}\n")
    guess = input("Who has more instagram followers? 'A' or 'B': ")

    return guess == correct_letter

def display_topic(topic):
    return f"{topic['name']} is a {topic['description']} from {topic['country']}."

score = 0
copy_of_data = data
game_is_over = False
while not game_is_over:
    print(art.logo)
    main_topic = get_topic(copy_of_data)
    copy_of_data.remove(main_topic)
    compare_topic = get_topic(copy_of_data)
    copy_of_data.remove(compare_topic)

    correct = start_game(main_topic, compare_topic)

    if not correct:
        again = input(f"Game over.\nScore: {score}\nPlay Again? y/n: ")
        score = 0
        clear()
        if again != "y":
            game_is_over = True
    else:        
        score += 1
        clear()

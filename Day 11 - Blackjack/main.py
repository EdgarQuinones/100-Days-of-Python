############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from art import logo

def draw_card(hand):
    new_card = random.choice(cards)
    hand.append(new_card)
    return hand

def get_score(hand):
    return sum(hand)
    
def get_hand():
    pair = []
    for _ in range(2):
        pair = draw_card(pair) 
    return pair

def print_cards(player, dealer):
    print(f"Your cards: {player}, current score: {get_score(player)}")
    print(f"Computer's first card: {dealer[0]}")

def players_turn(player, dealer):
    draw = True
    while draw:
        print_cards(player, dealer)
        reply = input("Type 'y' to get another card, type 'n' to pass: ")
        if reply == "y":
            player = draw_card(player)
            if over_21(player) and not has_ace(player):
                return False
            else:
                player = change_ace(player)
        else:
            return get_score(player)

def change_ace(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        return hand
        
            
def computers_turn(dealer, player):
    computers_score = get_score(dealer)
    players_score = get_score(player)
    
    while computers_score < 17 or computers_score < players_score:
        dealer = draw_card(dealer)
        computers_score = get_score(dealer)
        if over_21(dealer) and not has_ace(dealer):
            return False
        else:
            dealer = change_ace(dealer)
    return computers_score
    
def player_blackjack(hand):
    if get_score(hand) == 21:
        print("Black Jack! You got 21 in your first 2 cards!")
        return True
        
def computer_blackjack(hand):
    if get_score(hand) == 21:
        print("Black Jack! Your opponent got 21 in their first 2 cards!")
        return True

def over_21(hand):
    if get_score(hand) > 21:
        return True
    else:
        return False

def player_busted(player, dealer):
    final_print(player, dealer)
    print("You went over. You lose :(")

def dealer_busted(player, dealer):
    final_print(player, dealer)
    print("Your opponent went over. You win :D")

def game_won(player, dealer):
    final_print(player, dealer)
    print("You win :D")

def game_lost(player, dealer):
    final_print(player, dealer)
    print("You lost :(")

def game_draw(player, dealer):
    final_print(player, dealer)
    print("Draw.")

def final_print(player, dealer):
    print(f"Your final hand: {player}, final score: {get_score(player)}")
    print(f"Computer's final hand: {dealer}, final score: {get_score(dealer)}")

def has_ace(hand):
    for card in hand:
        if card == 11:
            return True
    return False

def game_status(players_cards, players_score, dealers_cards, dealers_score):
    if not dealers_score:
        dealer_busted(players_cards, dealers_cards)
    elif computer_blackjack(computers_cards):   
        return
    elif players_score > dealers_score:
        game_won(players_cards, dealers_cards)
    elif players_score < dealers_score:
        game_lost(players_cards, dealers_cards)
    else:
        game_draw(players_cards, dealers_cards)


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play_again = False
while not play_again:
    players_cards = []
    computers_cards = []
    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if again != "y":
        break

    print(logo)
    
    players_cards.extend(get_hand())
    computers_cards.extend(get_hand())

    if player_blackjack(players_cards):
        continue

    players_final_score = players_turn(players_cards, players_cards)

    if not players_final_score:
        player_busted(players_cards, computers_cards)
        continue
    
    computers_final_score = computers_turn(computers_cards, players_cards)

    game_status(players_cards, players_final_score, computers_cards, computers_final_score)

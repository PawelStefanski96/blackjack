#Initialize function to pick a card from deck
import random
import os
from blackjack_art import logo
def card_pick(deck):
    return random.choice(deck)

def check_winner(player_hand, computer_hand):
    if sum(player_hand) > 21:
        return 'You went over. You lost! 😪'
    elif sum(player_hand) == sum(computer_hand):
        return 'Draw 😵'
    elif sum(player_hand) == 21 and sum(computer_hand) != 21:
        return 'You won with a blackjack congratulations!!!! 🥳🥳🥳'
    elif sum(player_hand) < 21 and sum(computer_hand) > 21:
        return 'Computer went over. You won! 👌'
    elif sum(player_hand) > sum(computer_hand):
        return 'You have a better score than computer! You won! 🥳'
    else:
        return 'You lost 😱, better luck next time!'

def end_game(player_hand, computer_hand):
    os.system('cls')
    print(logo)
    print(f'Your cards: {player_hand}, current score: {sum(player_hand)}')
    print(f"Computer's first card: {computer_hand}, computer score: {sum(computer_hand)}")
    print(check_winner(player_hand, computer_hand))
from blackjack_art import logo
import os
from blackjack_functions import card_pick, end_game

#Initialize cards list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Initialize game loop
while True:

    #Print a logo and take input from player to start the game
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")

    #Player want to play a game go
    if game_start == 'y':
        #Pick a cards for computer and player
        player_hand = [card_pick(cards), card_pick(cards)]
        computer_hand = [card_pick(cards)]

        #Initialize the loop to check if player want to draw more cards
        while True:
            #Reset the screen and print logo
            os.system('cls')
            print(logo)

            if sum(player_hand) > 21:
                while sum(computer_hand) <= 15:
                    computer_hand.append(card_pick(cards))
                end_game(player_hand, computer_hand)
                break

            #Print player and computer hand at the beggining
            print(f'Your cards: {player_hand}, current score: {sum(player_hand)}')
            print(f"Computer's first card: {computer_hand[0]}")

            #Initialize the input to check if player want to draw next card
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
            

            #If player want next card add next card to the players hand from deck
            if continue_game == 'y':
                player_hand.append(card_pick(cards))


            #If player dont want to take next card computer draws cards and display game output
            elif continue_game == 'n':
                #Pick cards for computer end if computer hand > 15
                while sum(computer_hand) <= 15:
                    computer_hand.append(card_pick(cards))
                end_game(player_hand, computer_hand)
                break
                
    else:
        break
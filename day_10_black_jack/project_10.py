# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:14:15 2021

@author: bercy
BlackJack
"""
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
dealer =  []    

def initialize_game(game_on):   
    if game_on:
        print(logo)
        for i in range(2):
            user.append(random.choice(cards))
            dealer.append(random.choice(cards))
            
        print(f"Your card {user} current score: {sum(user)}")
        print (f"The dealer's first card is {dealer[0]} ")
        
    else:
        print("Ok, No game")
      
def print_stats(print_user, print_dealer): 

    if print_user:
        print(f"Your cards {user}, total {sum(user)}")
    if print_dealer:
        print(f"dealer's cards {dealer}, total {sum(dealer)}")     

def black_jack():
    
    game_on = True if input("Enter 'yes' to play: ") == 'yes' else False
    initialize_game(game_on)
        
    while(game_on):
       
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
       
        if user_input == 'n':
            print("checking for winnner:")
            
            while(sum(dealer) < 17  ):
                dealer.append(random.choice(cards))
                if(sum(dealer) > 21):
                    print_stats(True,True)
                    print("dealer bust, you win!")
                    return
            print_stats(True,True)

            if sum(user) == sum(dealer):
                print("It's a draw")
            elif sum(user) > sum(dealer):
                print("user wins")
            elif sum(user) < sum(dealer):
                print("dealer wins")
                
            game_on = False
            
        elif user_input == 'y':
            user.append(random.choice(cards))
            print_stats(True,False)


        if(sum(user) > 21):
            print_stats(False,True)
            print("Bust, You lose!")
            game_on = False

    
    
black_jack()

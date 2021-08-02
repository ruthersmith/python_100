# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:51:30 2021

@author: bercy
secret auction
"""
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def secret_auction():
    print(logo)
    are_more_bidders = True
    bidders =  {}
    print("welcome to the secret auction")
    
    while(are_more_bidders):
        name = input("what is your name: ")
        bid  = int(input("what is your bid: "))
        bidders[name] = bid
        are_more_bidders = input("are there more bidders: yes or no ") == "yes"
        
    winner = ""   
    for key in bidders:
        if len(winner) == 0:
            winner = key
        elif bidders[key] > bidders[winner]:
            winner = key
    print(f"winner is {winner} with a bid of {bidders[winner]}")
        
secret_auction()
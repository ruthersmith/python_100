# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:35:37 2021

@author: bercy

 -> rock paper scissor game   
 -> project 4
"""

#used by the random number generator in project 4, rock paper scissor
import random
 
    
#Rock  0 wins against scissors 2
#Scissors 2  win against paper 1
#Paper 1 wins against rock 0
    
# 0 = rock, 1 = paper, 2 = scissors
def project_4():
    
    user = int(input("what do you choose, type 0 for rock, 1 for paper, 2 for scissors: "))
    ai = random.randint(0,2)
    
    print_project4_ascii(user,"You ")
    print_project4_ascii(ai,"Computer ")
    
    check_project_4_winner(user,ai)

def check_project_4_winner(user,ai):
    
    if user == ai:
        print("it was a draw")
    elif (user == 0 and ai == 2) or (user == 2 and ai == 1) or (user == 1 and ai ==0) :
        print("user wins")
    else:
        print("computer wins")
    
def print_project4_ascii(x,player):
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    if  x == 0:
        print(f"{player} chose rock {rock}")
    elif x == 1:
          print(f"{player} chose paper {paper}")
    elif x == 2:
         print(f"{player} chose scissors {scissors}")
    else:
        print("unkown choice")
    
    
if __name__ == '__main__':
    project_4()

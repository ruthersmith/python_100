# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:33:10 2021

@author: bercy

Just some notes/reminder

attribute: variable associated with an object
in python __init__ function is used as a constructor
"""

class User:
    def __init__(self,id):
        self.id = id
        
    def follow(self):
        return "follow"

#initialize an object of class user
user_1 = User(1)
print(user_1.follow())
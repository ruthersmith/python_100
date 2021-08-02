# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:19:44 2021

@author: bercy
"""
 #Password Generator Project
import random

def fizzBuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0 :
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
#fizzBuzz()
            
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    total_characters = nr_letters + nr_symbols + nr_numbers
    
    password = []
    
    
    for char in range(total_characters):
        new_char = letters[random.randint(0,len(letters) - 1)]
        password.append(new_char)
        
    for i in range(nr_numbers):
        pass_index = random.randint(0,len(password) - 1)
        num_index = random.randint(0,len(numbers) - 1)
        password[pass_index] = numbers[num_index]
        
    for i in range(nr_symbols):
        pass_index = random.randint(0,len(password) - 1)
        symbol_index = random.randint(0,len(symbols) - 1)
        password[pass_index] = symbols[symbol_index]
        
    print("".join(password))

password_generator()
    
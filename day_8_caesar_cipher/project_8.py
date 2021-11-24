# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:20:37 2021

@author: bercy
Caesar cipher

Bring you an all time favorite,
This is my python implementation of a caesar cipher

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext 
is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.

When running the program,
it prompts the user for 3 user inputs to be typed in the console:
1) The task the user wants to perform either encrypt or decrypt
2) The plain text message
3) By how many letters should this message be shifted by


More Info on the caesar cipher :https://en.wikipedia.org/wiki/Caesar_cipher
"""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


    
def encrypt(text,shift):
    new_text_list = []
    text_list = list(text)
    
    for char in text_list:
        if alphabet.count(char):
            new_char_index = (alphabet.index(char) + shift) % 26
            new_text_list.append(alphabet[new_char_index])
        else:
            new_text_list.append(" ")
    print("".join(new_text_list))

def decrypt(text,shift):
    shift *= -1
    encrypt(text,shift)

def project_8():
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)
        
        
if __name__ == '__main__':
    project_8()
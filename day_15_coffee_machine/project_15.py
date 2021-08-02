# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:12:01 2021

@author: bercy
coffee machine
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")

def insert_coin_true(drink):
    quarters = int(input("please enter number of quarters: "))
    dimes = int(input("please enter number of dimes: "))
    nickels = int(input("please enter number of nickels: "))
    cents = int(input("please enter number of cents: "))
    
    total_amount = (quarters*.25) + (dimes*.1) + (nickels*.05) + (cents * .01)
        
    return round (total_amount -  MENU[drink]["cost"],2 )



def check_resources(drink):
    enough = True
    required_ingredient = MENU[drink]["ingredients"]
    
    for ingredient in required_ingredient:
        if resources[ingredient] < required_ingredient[ingredient]:
            print(f"sorry not enough {ingredient}")
            enough = False
            
    return enough

def make_coffee(drink):
    ''' ejenrer '''
    resources["money"] += MENU[drink]["cost"]
    required_ingredient = MENU[drink]["ingredients"]
    
    for ingredient in required_ingredient:
        resources[ingredient] -= required_ingredient[ingredient]
    
    

def main():
    resources["money"] = 0
    prompt = "What would you like? (espresso/latte/cappuccino): "
    while True:
        user_input = input(prompt)
        
        if user_input == "off":
            break
        
        elif user_input == "report":
            report()
        
        elif user_input == "latte" or user_input == "cappuccino" or user_input == "espresso":
            
            if not check_resources(user_input):
                continue
            
            give_back_amount = insert_coin_true(user_input)
           
            if(give_back_amount >= 0):
                make_coffee(user_input)
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        
if __name__ == '__main__':
        main()




















# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:13:09 2021

@author: bercy
"""

from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.speed("fastest")

def draw_square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)
  
def draw_dash_line():
    for i in range(15):     
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(20)
        my_turtle.pendown()
        
for i in range(100):
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + 5 )
        
#draw_dash_line()
#draw_square()

screen = Screen()
screen.exitonclick()




#draw_square(my_turtle)
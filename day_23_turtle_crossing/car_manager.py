from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    MAX_CARS = 75
    car_speed = 10

    def __init__(self):
        self.cars = []

    def generate_car(self):
        if len(self.cars) < CarManager.MAX_CARS:
            car = Turtle("square")
            car.setheading(180)
            car.shapesize(1.1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(x=280, y=random.randint(-280, 280))
            self.cars.append(car)

    def move_cars(self, turtle):
        """ Moves to car according to static class var car_speed"""
        for car in self.cars:
            car.forward(CarManager.car_speed)
            if car.xcor() < -380:
                car.clear()
                self.cars.remove(car)

    def exist_collision(self,player):
        for car in self.cars:
            if car.distance(player) < 20:
                print('game over')
                return True

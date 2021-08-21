import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

UP_KEY = "Up"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_forward, UP_KEY)
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
car_generator_frequency = 3
car_generator_frequency_counter = 0

while game_is_on:
    time.sleep(0.1)

    if player.ycor() > 280:
        car_manager.car_speed *= 2
        player.reset_pos()
        scoreboard.update_level()
    if car_generator_frequency_counter % car_generator_frequency == 0:
        car_manager.generate_car()
    if car_manager.exist_collision(player):
        game_is_on = False
        scoreboard.game_over()

    car_manager.move_cars(player)
    car_generator_frequency_counter += 1
    screen.update()

screen.exitonclick()

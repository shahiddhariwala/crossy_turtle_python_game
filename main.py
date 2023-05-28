import random
from turtle import Screen
from player import Player
from car import Car
import time

from score_board import ScoreBoard

screen = Screen()

screen.title("Crossy turtle")
screen.setup(width=600, height=500)
screen.tracer(0)

is_game_on = True
car_list = []
player = Player()
score_board = ScoreBoard()

screen.listen()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")
car_counter = 0
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_counter += 1

    if car_counter % 6 == 0:
        new_car = Car((270, random.choice(range(-200, 200, 20))))
        car_list.append(new_car)

    for car in car_list:
        car.move()
        if car.distance(player) < 50:
            score_board.game_over()
            is_game_on = False

    # Player reached top
    if player.ycor() > 230:
        score_board.update_level()
        player.reset_player_pos()

screen.exitonclick()

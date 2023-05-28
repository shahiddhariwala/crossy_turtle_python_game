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

car_1 = Car((270, 220))
player = Player()
score_board = ScoreBoard()

screen.listen()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

while is_game_on:
    time.sleep(0.1)
    screen.update()

    # Player reached top
    if player.ycor() > 230:
        score_board.update_level()
        player.reset_player_pos()

screen.exitonclick()

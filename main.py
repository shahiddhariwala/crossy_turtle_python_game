from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()

screen.title("Crossy turtle")
screen.setup(width=600, height=500)
screen.tracer(0)

is_game_on = True

car_1 = Car((270, 220))
player = Player()

screen.listen()

screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")


while is_game_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
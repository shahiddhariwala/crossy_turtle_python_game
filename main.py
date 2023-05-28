from turtle import Screen
from car import Car
screen = Screen()

screen.title("Crossy turtle")
screen.setup(width=600, height=500)
screen.tracer(0)

is_game_on = True

car_1 = Car((270, 220))

while is_game_on:
    screen.update()


screen.exitonclick()
from turtle import Turtle
import random

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Car(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.color(random.choice(rainbow_colors))
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move(self, speed = 10):
        self.forward(speed)

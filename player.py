from turtle import Turtle

MOVEMENT_SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_player_pos()

    def move(self):
        self.forward(MOVEMENT_SPEED)

    def reset_player_pos(self):
        self.goto(0, -230)

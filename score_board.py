import turtle

FONT = ("fira-sans", 18, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 220)
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def update_level(self):
        self.level += 1
        self.score += 1
        self.update_score_board()
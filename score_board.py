import turtle

FONT = ("fira-sans", 18, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 220)
        self.game_speed = 0.1
        self.level = 1
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def update_level(self):
        self.level += 1
        self.game_speed *= 0.8
        self.update_score_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over! Level: {self.level}", False, "center", FONT)

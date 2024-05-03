from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("Green")
        self.goto(0, 350)
        self.hideturtle()
        self.score_set()

    def score_set(self):
        self.write(f"Level : {self.level}", align="center", font=("arial", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.score_set()

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("Game Over", align="center", font=("arial", 60, "normal"))

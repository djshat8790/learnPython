from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-50, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("", 13, ""))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

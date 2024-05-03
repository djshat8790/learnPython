from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 0)
        self.write(self.l_score, font=("Arial", 80, "normal"))
        self.goto(100, 0)
        self.write(self.r_score, font=("Arial", 80, "normal"))

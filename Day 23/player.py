from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("#D21F3C")
        self.goto(0, -265)
        self.setheading(90)

    def move_player(self):
        self.forward(40)

    def player_reset(self):
        self.goto(0, -265)

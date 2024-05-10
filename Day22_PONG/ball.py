import random
from turtle import Turtle

move = [-1, 1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        new_direction = random.choice(move)
        self.x_move = 10 * new_direction
        self.y_move = 10 * new_direction

    def move_ball(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.bounce_wall()

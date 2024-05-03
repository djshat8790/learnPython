from turtle import Screen, Turtle

from score import Score
from paddle import Paddle
from ball import Ball
import time

is_game_on = True

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
line = Turtle()
line.penup()
line.goto(0, 0)
line.color("white")
line.shape("square")
line.shapesize(stretch_wid=30, stretch_len=1 / 20)

score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while is_game_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.1)

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_paddle()

    if ball.xcor() > 370:
        ball.refresh()

    if ball.xcor() < -380:
        ball.refresh()

screen.exitonclick()

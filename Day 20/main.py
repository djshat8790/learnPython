from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time
is_game_on = True

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

screen.exitonclick()

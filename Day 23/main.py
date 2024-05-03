from turtle import Screen
from player import Player
from cars import Cars
from road import Road
from scoreboard import Score
import time

# Screen code
screen = Screen()
screen.setup(width=1000, height=800)
screen.screensize(canvwidth=800, canvheight=600, bg="blue")
screen.bgcolor("Black")
screen.title("Turtle crossing")
screen.tracer(0)

# objects
player = Player()
car = Cars()
road = Road()
score = Score()

# screen listen
screen.listen()
screen.onkeypress(player.move_player, "Up")

is_game_on = True
loop_count = 1
while is_game_on:
    loop_count += 1
    screen.update()
    time.sleep(0.1)
    if loop_count == 5:
        car.create_car()
        loop_count = 0
    car.move_car()
    for cars in car.car_list:
        if cars.distance(player) < 30:
            is_game_on = False
            score.game_over()
    if player.ycor() == 295:
        player.player_reset()
        car.car_speed += 5
        score.level_up()


screen.exitonclick()

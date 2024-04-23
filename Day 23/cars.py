
from turtle import Turtle
import random

CAR_POSITION = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260]
CAR_COLOR = ["red", "magenta", "yellow", "blue", "purple", "pink", "violet", "indigo", "orange", "cyan"]


class Cars:

    def __init__(self):
        self.car_list = []
        self.create_car()
        self.car_speed = 10

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("turtle")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(CAR_COLOR))
        car.setheading(180)
        car.goto(480, random.choice(CAR_POSITION))
        self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

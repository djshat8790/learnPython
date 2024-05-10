from turtle import Turtle
from cars import CAR_POSITION


class Road:

    def __init__(self):
        self.create_road()
        self.road_patch()
        self.new_finish_line()

    @staticmethod
    def create_road():
        for car in CAR_POSITION:
            road = Turtle()
            road.penup()
            road.shape("square")
            road.shapesize(stretch_wid=1 / 4, stretch_len=45)
            road.color("Gray")
            road.goto(0, car - 20)

    @staticmethod
    def road_patch():
        for patch in CAR_POSITION:
            new_patch = Turtle()
            new_patch.penup()
            new_patch.color("white")
            new_patch.goto(-450, patch)
            new_patch.hideturtle()
            for i in range(1, 55):
                if i % 5 == 0:
                    new_patch.pendown()
                    new_patch.forward(5)
                else:
                    new_patch.up()
                    new_patch.forward(20)

    @staticmethod
    def new_finish_line():
        road = Turtle()
        road.shape("square")
        road.goto(-450, CAR_POSITION[-1] + 20)
        road.hideturtle()
        for i in range(1, 31):
            if i % 2 == 0:
                road.color("white")
            else:
                road.color("red")
            road.forward(30)



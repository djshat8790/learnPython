from turtle import Turtle
from cars import CAR_POSITION


class Road:

    def __init__(self):
        self.create_road()
        self.road_patch()
        self.finish_line()

    @staticmethod
    def create_road():
        for car in CAR_POSITION:
            road = Turtle()
            road.penup()
            road.shape("square")
            road.shapesize(stretch_wid=1 / 4, stretch_len=45)
            road.color("#4f7942")
            road.goto(0, car - 20)

    @staticmethod
    def road_patch():
        for patch in CAR_POSITION:
            new_patch = Turtle()
            new_patch.penup()
            new_patch.color("white")
            new_patch.goto(-450, patch)
            new_patch.hideturtle()
            for i in range(0, 45):
                if i % 2 != 0:
                    new_patch.pendown()
                else:
                    new_patch.up()
                new_patch.forward(20)

    def finish_line(self):
        road = Turtle()
        writing = Turtle()
        writing.penup()
        road.penup()
        road.shape("square")
        road.shapesize(stretch_wid=1 / 4, stretch_len=45)
        road.color("#4f7942")
        road.goto(0, CAR_POSITION[-1] + 20)
        writing.goto(0, CAR_POSITION[-1] + 40)
        writing.color("#01796F")
        writing.hideturtle()
        writing.write("Finish Line", align="center", font=("arial", 40, "normal"))

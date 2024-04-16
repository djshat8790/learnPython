import random
import turtle
from turtle import Turtle, Screen
import colorgram

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
# timmy_the_turtle.speed("fastest")
turtle.colormode(255)
# direction = [0, 90, 180, 270]

rgb_colors = []


def extract_color():
    colors = colorgram.extract("py.jpg", 50)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


def new_art():
    extract_color()
    timmy_the_turtle.speed(100)
    timmy_the_turtle.penup()
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.setheading(225)
    timmy_the_turtle.forward(300)
    timmy_the_turtle.setheading(0)
    for color in range(1, 101):
        timmy_the_turtle.dot(20, random.choice(rgb_colors))
        timmy_the_turtle.forward(50)
        if color % 10 == 0:
            timmy_the_turtle.setheading(90)
            timmy_the_turtle.forward(50)
            timmy_the_turtle.setheading(180)
            timmy_the_turtle.forward(500)
            timmy_the_turtle.setheading(0)


new_art()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# def draw_circle():
#     for i in range(72):
#         timmy_the_turtle.color(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(i*20)

#
# for i in range(1000):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.setheading(random.choice(direction))
#
# for i in range(8):
#     timmy_the_turtle.color(color[i])
#     for j in range(i+3):
#         timmy_the_turtle.forward(100)
#         angel = 360/(i+3)
#         timmy_the_turtle.right(angel)

scree = Screen()
scree.exitonclick()

import random
from turtle import Turtle, Screen
from tkinter import messagebox


screen = Screen()
screen.title("Welcome to Turtle Race")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
turtle_colors = ["red", "green", "yellow", "blue", "purple", "orange"]
turtle_coordinates = [-200, -100, 0, 100, 200, 300]
turtle_name = ["Tim", "Tom", "Tiny", "Tony", "Toby", "Terry"]


def race_begin():
    is_game_on = True
    next_game = True
    while next_game:
        screen.reset()
        turtle_list = []
        user_bet = screen.textinput(title="Make your bet: ",
                                    prompt=f"Which turtle will win the race? \n{turtle_colors}\nEnter a color: ")
        for i in range(6):
            turtle_obj = Turtle()
            turtle_obj.penup()
            turtle_obj.shape("turtle")
            turtle_obj.color(turtle_colors[i])
            turtle_obj.goto(-440, turtle_coordinates[i])
            turtle_obj.write(turtle_name[i], font=("", 25, ""), align="right", move=True)
            turtle_list.append(turtle_obj)


        if user_bet:
            is_game_on = True

        while is_game_on:
            for turtle in turtle_list:
                distance = random.randint(0, 20)
                turtle.forward(distance)
                if turtle.xcor() > 450:
                    is_game_on = False
                    next_game = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        messagebox.showinfo(title="WINNER !", message=f"You win. {} {winning_color} turtle is the winner")
                    else:
                        messagebox.showinfo(title="LOOSER !", message=f"You lose. {winning_color} turtle is the winner")
        user_input = screen.textinput(title="Turtle Race ",
                                      prompt="Want to play another game? Type 'Yes' or 'No'")
        if user_input.lower() == "yes":
            next_game = True



race_begin()
screen.exitonclick()

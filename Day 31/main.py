import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/spanish_words.csv")
data_list = data.to_dict(orient="records")
counter = 3
data_dict = {}


# ----------------------------Impl -------------------------------

def button_press():
    global data_dict, window_timer
    window.after_cancel(window_timer)
    data_dict = random.choice(data_list)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(words, text=f"{data_dict["Spanish"]}", fill="black")
    count_down(count=counter)
    canvas.itemconfig(card_background, image=front_card_image)


def english_version():
    canvas.itemconfig(card_background, image=back_card_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(words, text=f"{data_dict["English"]}", fill="white")

def count_down(count):
    global window_timer
    canvas.itemconfig(timer, text=count)
    if count > 0:
        window_timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        canvas.itemconfig(timer, text="")
        english_version()


def game_start_mess():
    canvas.itemconfig(language, text="Improve your Spanish")


# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window_timer = window.after(100, game_start_mess)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_image)
language = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
words = canvas.create_text(400, 263, text="Click any button", font=("ariel", 60, "bold"))
timer = canvas.create_text(400, 50, text="", font=("ariel", 40, "bold"), fill="red")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")
cross_button = Button(image=cross_button_image, highlightthickness=0, command=button_press)
cross_button.grid(column=0, row=1)
right_button = Button(image=right_button_image, highlightthickness=0, command=button_press)
right_button.grid(column=1, row=1)

window.mainloop()

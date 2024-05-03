from tkinter import *

window = Tk()
window.title("Miles To KM Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to: ")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label4 = Label(text=0)
label4.grid(column=1, row=1)


# Button
def button_clicked():
    miles = float(user_input.get())
    km = round(miles * 1.609344, 6)
    label4.config(text=km)


button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2)

# Entry

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

window.mainloop()
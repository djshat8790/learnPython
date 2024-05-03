import json
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            message = data[website]
    except FileNotFoundError:
        messagebox.showerror("Oops", message="No password saved yet")
    except KeyError:
        messagebox.showerror("Oops", message="no such website exists")
    else:
        messagebox.showinfo("Data", message=f"Email: {message["email"]}\nPassword: {message["password"]}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError as error:
            print(f"{error}: No such file exist")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=45)
username_entry.insert(0, "dheeraj.shukla8790@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()

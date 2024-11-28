import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- FIND INFORMATION ------------------------------- #
def find_password():
    """
    Searches for the password for the website
    the user specified in the JSON file, and returns the password for that website.

    If no website is found, it outputs an error message stating nothing was found.
    """
    website = entry_website.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email_username = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title="Current Information", message=f"Email/Username: {email_username}"
                                                                     f"\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message="No entry found for that website.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """
    Using a password generator algorithm, the method creates a random password
    using uppercase/lowercase letters, numbers, and symbols, leading to
    a random, completely unique password everytime.

    When the user clicks "Generate Password", it is also automatically copied to
    their clipboard, in case they want to use it right away.
    """
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)

    # Copies password to your clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """
    When the user inputs a website a password, they can save it with the
    "add" button. It will create a new JSON file, and add it there. It
    will replace repeats, but it is CASE SENSITIVE, so 'facebook' and
    'Facebook' are NOT the same.

    NOTE: It is highly recommended if you use this, to encrypt the file in between
    uses so your passwords aren't stored in plain text.
    """
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:

        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)

        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(END, "bob123@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()

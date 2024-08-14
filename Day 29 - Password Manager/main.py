from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
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
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        okay_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                                     f"\nEmail: {email}"
                                                                     f"\nPassword: {password}"
                                                                     f"\n\nIs it okay to save?")
        if okay_to_save:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

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
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

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

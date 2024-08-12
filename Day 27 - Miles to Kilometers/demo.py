#
# # Unlimited Arguments
# def add(*args):
#     for n in args:
#         print(n)
#
#
# # Default arguments
# def print_3_nums(a, b=3, c=4):
#     print(a, b, c)
#
# # Any number of keyword arguments
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     stuff
#
#     print(kwargs["add"])
#
# calculate(2, add=3, mutiply=5)
#
# class Car:
#     def __init__(self, seats=2, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.model = seats
# my_car = Car(make="Nissan")
# print(my_car.model)

from tkinter import *


def button_clicked():
    input_text = input_field.get()
    my_label.config(text=input_text)


window = Tk()
window.title("FIRST GUI EVER")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="New text")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

# Button
button = Button(text="old button", command=button_clicked)
button.grid(column=1, row=1)
button.config(pady=40, padx=40)

button2 = Button(text="new button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)

window.mainloop()

import random
import tkinter as tk
from tkinter import ttk
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE FLASH CARDS ------------------------------- #
words = pandas.read_csv("data/japanese_words.csv")


def new_word():
    random_number = random.randint(0, 99)
    english_word = words["English"][random_number]
    japanese_word = words["Japanese"][random_number]

    title_label.config(text="Japanese")
    word_label.configure(text=japanese_word, anchor="center")


def flip_card():
    random_number = random.randint(0, 99)
    english_word = words["English"][random_number]
    title_label.config(text="English")
    word_label.configure(text=english_word, anchor="center")


# ---------------------------- UI SETUP ----------------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
window.minsize(width=820, height=670)

canvas = tk.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
canvas.create_image(400, 300, image=card_front)
canvas.place(x=0, y=-30)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, bd=0, command=flip_card)
wrong_button.place(x=150, y=535)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, bd=0, command=new_word)
right_button.place(x=500, y=535)

title_label = tk.Label(text="Japanese", font=("Helvetica", 30, "italic"), bg="white")
title_label.place(x=280, y=150)

word_label = ttk.Label(text="Word", font=("Helvetica", 50, "bold"), background="white", anchor="center")
word_label.place(x=250, y=250)

window.mainloop()

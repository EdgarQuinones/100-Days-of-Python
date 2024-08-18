import random
import tkinter as tk
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_review = []

# ---------------------------- WORDS TO LEARN FILE ------------------------------- #

try:
    # Find words_to_learn.csv
    with open("words_to_learn.csv", mode="r") as file:
        content = file.readlines()
        to_learn = pandas.read_csv(file).to_dict()
except FileNotFoundError:
    # Create new file
    words_to_learn_file = open("words_to_learn.csv", mode="w")

    data = pandas.read_csv("data/japanese_words.csv")
    to_learn = data.to_dict(orient="records")

current_card = random.choice(to_learn)


# ---------------------------- CREATE FLASH CARDS ------------------------------- #
def next_card():
    global current_card, flip_timer, to_learn

    window.after_cancel(flip_timer)

    if len(to_learn) > 0:

        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="Japanese", fill="black")
        canvas.itemconfig(card_word, text=current_card["Japanese"], fill="black")
        canvas.itemconfig(canvas_image, image=card_front)

        flip_timer = window.after(3000, flip_card)
    else:

        for card in to_review:
            words_to_learn_file.write(f"{card}\n")
        exit()


def remove_card():
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        next_card()


def review_card():
    global to_review

    to_review.append(current_card)

    if len(to_learn) > 0:
        to_learn.remove(current_card)

    next_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ----------------------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, bd=0, command=review_card)
wrong_button.grid(column=0, row=1, padx=50)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, bd=0, command=remove_card)
right_button.grid(column=1, row=1, padx=50)

next_card()

window.mainloop()

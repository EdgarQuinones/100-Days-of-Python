import random
import time
import tkinter as tk
from contextlib import nullcontext
from email.policy import default
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

"""
Trys to find the words_to_learn file 
containing all the words the user got wrong,
if it is not found, it will use a brand new 
list.
"""
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (pandas.errors.EmptyDataError, FileNotFoundError):
    original_data = pandas.read_csv("data/japanese_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- CREATE FLASH CARDS ------------------------------- #
def next_card():
    """
    Goes to the next card in the deck, shows the question side,
    waits 3 seconds, and then calls the flip_card function
    which flips it to the answer side
    """
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_word, text=current_card["Japanese"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)

    flip_timer = window.after(3000, flip_card)

def is_known():
    """
    If the user correctly chooses the card, it will
    be removed from the "to_learn" dictionary. Once
    the user finishes the current list of cards, it
    will leave a list of words that need to be learned
    """
    to_learn.remove(current_card)

    word_to_learn_file = pandas.DataFrame(to_learn)
    word_to_learn_file.to_csv("data/words_to_learn.csv", index=False)

    if len(to_learn) == 0:
        canvas.itemconfig(canvas_image, image=card_back)
        canvas.itemconfig(card_title, text="All Cards Learned!", fill="white")
        canvas.itemconfig(card_word, text="Congrats", fill="white")
        right_button["state"] = "disabled"
        wrong_button["state"] = "disabled"

    else: next_card()


def flip_card():
    """
    Flips the card from the question side, to the answer side
    """
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
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1, padx=50)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=1, row=1, padx=50)

next_card()

window.mainloop()

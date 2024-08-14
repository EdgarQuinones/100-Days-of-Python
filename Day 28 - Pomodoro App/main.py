from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 450
reps = 1
CHECKMARK = "✓"
STARTING_TIMER = "25:00"
RESET = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Can use this function instead
    # window.after_cancel(timer)

    global reps
    global RESET
    RESET = True
    reps = 1
    count_down(0)
    canvas.itemconfig(timer_text, text=STARTING_TIMER)
    title_label.config(text="Timer", fg="Black")
    checkmark_label["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global RESET

    if reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        RESET = False
        count_down(WORK_MIN)
    elif reps % 2 == 0 and reps != 8:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
        checkmark_label["text"] += CHECKMARK
    else:
        title_label.config(text="Rest", fg=RED)
        count_down(LONG_BREAK_MIN)
        reps = 0
        checkmark_label["text"] = ""
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global RESET
    if RESET:
        return

    minutes = count // 60
    if minutes < 10:
        minutes = f"0{minutes}"

    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        # This can be a variable you reset
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text=STARTING_TIMER, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10))
checkmark_label.grid(column=1, row=2)

window.mainloop()

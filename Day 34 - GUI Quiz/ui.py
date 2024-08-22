from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.updated_text = self.canvas.create_text(150, 125, width=280, text="Question?", font=("Ariel", 12, "bold"))

        self.score = 0
        self.score_label = Label(fg="white", text=f"Score: {self.score}", padx=50, pady=10, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=self.false_answer)
        self.wrong_button.grid(column=0, row=2, padx=50, pady=20)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, bd=0, command=self.true_answer)
        self.right_button.grid(column=1, row=2, padx=50, pady=20)

        self.change_text()

        self.window.mainloop()

    def change_text(self):
        self.canvas.config(bg="white")

        try:
            new_text = self.quiz.next_question()
        except IndexError:
            self.right_button.destroy()
            self.wrong_button.destroy()
            self.score_label.destroy()
            self.canvas.itemconfig(self.updated_text, text=f"Final Score: {self.score}/10")
        else:
            self.canvas.itemconfig(self.updated_text, text=new_text)

    def false_answer(self):
        self.check_answer(self.quiz.check_answer("false"))

    def true_answer(self):
        self.check_answer(self.quiz.check_answer("true"))

    def check_answer(self, correct: bool):
        if correct:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.change_text)

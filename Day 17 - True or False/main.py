# This project is used to show how to use
# OOP in python. All classes were made from
# scratch and allow the user to use a set of
# data to ask a player a set of true/false
# questions. It also works with long answer
# questions if the player inputs the exact
# answer correctly.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for index in range(len(question_data["results"])):
    question = Question(question_data["results"][index]["question"], question_data["results"][index]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.next_question():
    quiz.next_question()

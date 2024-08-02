import random


class QuizBrain:
    """Handles the logic for the true/false game.
    Using a Question list, it can check how long left the game will
    last and return True once the game is over. Run this class in
    the main file using a while loop."""

    def __init__(self, question_list):
        """Each quiz will have number of questions,
        a question list, and a score."""

        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.temp_question_list = self.question_list

    def check_answer(self, user_answer, correct_answer):
        """Checks if the user got the question right and
        increases the score if so."""

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct! :D")
        else:
            print("Wrong! D:")
        print(f"New score: {self.score}/{self.question_number}")

    def still_has_questions(self):
        """Returns true if there still are questions left in the list"""
        return self.question_number < len(self.temp_question_list)

    def next_question(self):
        """Goes to the next question in the list and asks the user if there
        are any. If not returns True."""
        if self.still_has_questions():
            current_challenge = random.choice(self.temp_question_list)
            self.temp_question_list.remove(current_challenge)

            current_question = current_challenge.text
            current_answer = current_challenge.answer
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question} (True/False)?: ")
            self.check_answer(user_answer, current_answer)

            return True
        else:
            print(f"Game Over. Final Score: {self.score}")
            self.temp_question_list = self.question_list

            return False

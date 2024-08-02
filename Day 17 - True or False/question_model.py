class Question:
    """Stores a question, and an answer of a problem.
    Can be true/false or long answer"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Question:
    def __init__(self , question: str , correct_answer: str , choices: list):
        self.question_text: question
        self.correct_anwer: correct_answer
        self.choices: choices
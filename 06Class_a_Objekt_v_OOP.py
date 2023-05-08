class Question:

    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer


q_1 = Question("Python vznikl v roce 1991", "True")
print(q_1.text)
print(q_1.answer)

import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option letter): ")
        return user_answer.upper()

    def run_quiz(self):
        print("Welcome to the CodeSoft Python Quiz!\n")
        random.shuffle(self.questions)  # Shuffle questions for variety
        for question in self.questions:
            user_answer = self.display_question(question)
            correct_answer = question["correct_option"]

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}: {question['options'][ord(correct_answer) - ord('A')]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


# Sample quiz questions
python_quiz_questions = [
    {
        "question": "What is Python?",
        "options": ["A snake", "A programming language", "A type of tree", "A country"],
        "correct_option": "B",
    },
    {
        "question": "What is the purpose of the 'if' statement in Python?",
        "options": ["To loop over a sequence of items", "To define a function", "To make decisions", "To print a message"],
        "correct_option": "C",
    },
    {
        "question": "Which of the following is not a valid data type in Python?",
        "options": ["int", "float", "string", "char"],
        "correct_option": "D",
    },
]

if __name__ == "__main__":
    codesoft_quiz = QuizGame(python_quiz_questions)
    codesoft_quiz.run_quiz()

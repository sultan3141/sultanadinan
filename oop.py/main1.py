from question_model import Question
from question import question_data
from question_brain import QuizBrain  

# Create a question bank from the question data
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Loop through all questions in the quiz
while quiz.still_has_questions():
    quiz.next_question()

# Print the final results
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
        
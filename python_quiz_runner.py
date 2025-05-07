# import the random library to shuffle questions
import random

# load the questions from file
def load_questions(filename):
    with open(filename, "r") as file:
        content = file.read()
    blocks = content.strip().split("---\n")
    quizzes = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 6:
            quizzes.append(lines)
    return quizzes

# set the filename and load the questions
filename = "quiz_bank.txt"
questions = load_questions(filename)

# shuffle the questions randomly
random.shuffle(questions)

# set the initial score to 0 and a welcome message to the user
score = 0
print("Welcome to the Quiz Game!")

# go through each question and ask the user and its answer
for q in questions:
    print("\n" + q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    answer = input("Your answer (a/b/c/d): ").strip().lower()
    correct_answer = q[5].split(": ")[1].strip().lower()

# check if the answer is correct and update the score
    if answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is", correct_answer + ".\n")
        
# ask the user if they want to continue
# show the final score after the quiz ends
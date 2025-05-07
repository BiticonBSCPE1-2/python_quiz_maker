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
# shuffle the questions randomly
# set the initial score to 0 and a welcome message to the user
# go through each question and ask the user and its answer
# check if the answer is correct and update the score
# ask the user if they want to continue
# show the final score after the quiz ends
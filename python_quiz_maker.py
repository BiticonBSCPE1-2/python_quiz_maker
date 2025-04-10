# define a function to save question, options, and answer to a file
def questions(filename, question, options, correct_answer):
    with open(filename, "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"a. {options['a']}\n")
        file.write(f"b. {options['b']}\n")
        file.write(f"c. {options['c']}\n")
        file.write(f"d. {options['d']}\n")
        file.write(f"Answer: {correct_answer}\n")
        file.write("---\n")

# display a title and set the output filename
print("Quiz Creator!")
filename = "quiz_bank.txt"

# loop: ask for question, options (a-d), and the correct answer
# save the question to file and ask if the user wants to continue or stop
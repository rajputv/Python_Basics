import sys
import random

if len(sys.argv) < 2:
	print("Please supply a flash card file.")
	exit(1)

flashcard_file = sys.argv[1]
f = open(flashcard_file,"r")

question_dict = {}

for line in f:
	entry = line.strip().split(",")
	question = entry[0]
	answer = entry[1]
	question_dict[question] = answer

f.close()

print("Welcome to the flashcard game.")
print("If bored, type 'quit' to quit.")

questions = list(question_dict.keys())
while True:
	question = random.choice(questions)
	answer = question_dict[question]
	
	print("Question :" + question)
	user_input = raw_input("Your_Guess: ")
	if user_input == "quit":
		print("Thanks for playing, see you soon!!..")
		break
	elif user_input == answer:
		print("Correct!")
	else:
		print("Oops Incorrect!!")
		print("The answer is: "+ answer)


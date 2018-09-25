#Rock Paper Scissors
import random
print("Let's play Rock Paper Scissors! What is your choice?")
options = ["r", "p", "s"]
computer_choice = random.choice(options)
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

#Run Conditionals
if (user_choice == computer_choice):
	print("You're even.")
elif (user_choice == "s" and computer_choice == "p"):
	print("You chose scissors.  The computer chose paper.")
	print("You're a winner baby!")
elif (user_choice == "r" and computer_choice == "s"):
	print("You chose rock.  The computer chose scissors.")
	print("You're a winner baby!")
elif (user_choice == "p" and computer_choice == "r"):
	print("You chose paper.  The computer chose rock.")
	print("You're a winner baby!")
elif (user_choice == "s" and computer_choice == "r"):
	print("You chose scissors.  The computer chose rock.")
	print("You lose.")
elif (user_choice == "r" and computer_choice == "p"):
	print("You chose rock.  The computer chose paper.")
	print("You lose.")
elif (user_choice == "p" and computer_choice == "s"):
	print("You chose paper.  The computer chose scissors.")
	print("You lose.")
else:
	print("I don't understand that!")
	print("Next time, choose from 'r','p',or 's'").
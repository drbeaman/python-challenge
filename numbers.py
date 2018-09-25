#How many numbers?
user_play = "y"
while user_play == "y":

	user_number = input("How many numbers? ")
	
	#loop through the numbers.  Be sure to cast the string into an integer.	
	for x in range(int(user_number)):
		print(x)
	user_play = input("Continue: (y)es or (n)o? ")
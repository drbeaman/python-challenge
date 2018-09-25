#1warmup
print("Hello user!")
print("What is your name?")

user_name = input(user_name)

print("Hi " + user_name + "!")

user_age = input(user_age)
print("What is your age?")

user_age = int(input(user_age))

If (user_age) < 10:
	print("YOU ARE A BABY.")
Elif (user_age) >=11 and (user_age) <= 50:
	print("Cute for you.")
Else:
	print("YOU ARE OLD AS DIRT.")
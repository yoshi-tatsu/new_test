list = [1,2,3,4]

while True:
	x = input("type a number or q to quit.")
	if x == "q":
		break
	try:
		x = int(x)
	except ValueError:
		print("You have to type a number")
	if x in list:
		print("You guessed correctly!!")
	else:
		print("You guessed incorrectly.")


import random
playerNumber = 0
computerNumber = random. randint(1,51)
while(computerNumber != playerNumber):
	playerNumber = int(input("Please guess a number between 1 and 50: "))
	if (playerNumber < computerNumber):
		print("Guess higher!")
	elif (playerNumber > computerNumber):
		print("Guess lower!")
	else:
		print("Congratulations!")
 
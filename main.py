import random

gameover = False

while not gameover:
	computer = random.randint(0, 10)
	player = -1
	tries = 0
	while player != computer:	
		player = int(input("Guess a number: "))
		tries += 1
		if player == computer:
			print(f"You guessed it in {tries} tries.")
		elif player > computer:
			print("Too high")
		elif player < computer:
			print("Too low")
	choice = input("Play again? (y or n) ")
	if choice != "y":
		gameover = True
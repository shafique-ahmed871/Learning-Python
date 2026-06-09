# random modulo for random number
import random
# method for guessing number
def guessNumber() :

	#Generating random integer number b/w 1 to 100

	actualNumber = random.randint(1 , 100)


	# while loop for taking and comparing number with random number

	attempt = 0

	while True :
		attempt += 1
		try :
			guessNum = int(input("Guess the number(1-100) :"))
		except ValueError :
			print("please!, Enter a valid number")
			attempt -= 1
			continue

		if guessNum < 1 or guessNum > 100 : 
			print("Enter number b/w 1 and 100")
			attempt -= 1
		# checking whether number is high
		elif guessNum > actualNumber :
			print("Too high! Try again:", end = " ")
		elif guessNum < actualNumber :
			print("Too low! Try again:", end = " ")
		else :
			print(f"Correct! You guessed in {attempt} attempts")
			break

guessNumber()

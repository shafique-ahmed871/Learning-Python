def checkBalance(balance) :
	print(f"Net balance: {balance}")

def depositBalance(balance) :
	try :
		amount = float(input("Enter amount: "))

		if amount > 0:
			balance += amount
			print("Deposit! new balance:" , balance)
			return balance 
		else :
			print("amount must be greater than 0")
			return balance
	
	except ValueError :
		print("Invalid amount type!, try again")
		return balance
	
def withdrawBalance(balance) :
	try :
		amount = float(input("Enter amount: "))
		if amount > 0 :
			if amount > balance :
				print("Insuficient Balance")
				return balance
			balance -= amount
			print("Withdrawn! Remaining balance:" , balance)
			return balance
		else :
			print("amount must be greater than 0")
			return balance

	except ValueError :
		print("invalid amount type, try again!")
		return balance
		
		
def machine() :
	balance = 1500
	actual_pin = "0507"
	while True :

		enter_pin = input("Enter PIN:")

		if actual_pin == enter_pin :
			while True :
				print("1. Check Balance")
				print("2. Deposit")
				print("3. Withdraw")
				print("4. Exit")
				
				try :
					choice = int(input("Choose option: "))
					if choice >= 1 and choice <= 4 :
						if choice == 1 :
							checkBalance(balance)
						elif choice == 2 :
							balance = depositBalance(balance)
							
						elif choice == 3 :
							balance = withdrawBalance(balance)
							
						elif choice == 4 :
							print("GoodBye!")
							break
					else :
						print("Enter choice 1-4!")
				except ValueError :
					print("Invalid choice! try again")
		else :
			print("Invalid PIN, try again!")
			continue
		break


machine()
		
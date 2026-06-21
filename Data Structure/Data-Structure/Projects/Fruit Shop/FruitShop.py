def displayFruits() :
	fruits = [
		{'name' : 'Apple' , 'price' : 50},
		{'name' : 'Banana' , 'price' : 30},
		{'name' : 'Mango' , 'price' : 120},
		{'name' : 'Grapes' , 'price' : 200},
		{'name' : 'Orange' , 'price' : 80}
		]
	print("--- Available Fruits ---")
		
	for fruit in fruits :
		print(f"{fruit['name']}{' '*(8 - len(fruit['name']))}: Rs.{fruit['price']}/Kg")
	
	return fruits

def buyFruits(fruits , buyItem) :
	
	fruit_name = input("Enter fruit name: ").lower()
	isAvail = False 
	for fruit in fruits :
		if fruit['name'].lower() == fruit_name :
			isAvail = True
			
			try : 
				quantity = int(input("Enter quantity (Kg): "))

			except ValueError :
				print("Enter quantity in number: ")
				return buyItem
			if quantity <= 0:
				print("quantity must be greater than 0!")
				return buyItem
			fruit['quantity'] = quantity
			print(f"{fruit_name}	x{quantity}Kg added!")
			buyItem.append(fruit)
			return buyItem
				
	if not isAvail :
		print(f"sorry, {fruit_name} is not available")
		
		return buyItem

def receipt(buyItem) :
	if not buyItem :
		print("not buy any fruit!")
		return 
	print("--- Receipt ---")
	totalBill = 0
	for i in buyItem :
		print(f"{i['name']}{' ' * (8 - len(i['name']))}{i['quantity']}Kg  x  Rs.{i['price']} =  Rs.{i['price'] * i['quantity']}")
		totalBill += i['price'] * i['quantity']
	print(f"Total{' ' * (24 - len('Total'))}:  Rs.{totalBill}")
	print("Thankyou!")

def display() :
	print("=== Fruit Shop ===")
	buyItem = []
	fruits = displayFruits()
	print("\n\n")
	while True :

		buyMore = True
		while True :
			buy = input("do you want to buy: ")
			if buy.lower() == "yes" :
				buyItem = buyFruits(fruits , buyItem)
			elif buy.lower() == "no" :
				buyMore = False
				break
			else :
				print("Enter only (yes/no): ")
		if not buyMore :
			break
	receipt(buyItem)

display()

	
	

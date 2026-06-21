def addItem(items) :
	item = {}
	name = input("Enter item name: ")
	item["name"] = name
	try :
		price = float(input("Enter price: "))
	except ValueError :
		print("invalid price, should be in numbers!")
		return items
	try :
		quantity = int(input("Enter quantity: "))
	except ValueError :
		print("Invalid quantity")
		return items
	if price <= 0 :
		print("price must be > 0!")
		return items
	item["price"] = price
	if quantity <= 0 :
		print("quantity must be > 0!")
		return items
	item["quantity"] = quantity
	items.append(item)
	print(f"{name} is added to cart!")
	return items


def removeItem(items) :
	name = input("Enter item to be removed: ").lower()
	isAvail = False
	for item in items :
		if item["name"].lower() == name :
			items.remove(item)
			isAvail = True
			break
	if not isAvail : 
		print(f"{name} is not in Cart!")
	return items

def showCart(items) :
	if not items :
		print("Cart is empty!")
		return 
	print("--- Your Cart ---")
	for item in items :
		print(f"{item['name']}	x{item['quantity']}   = {item['price'] * item['quantity']}")

	
def bill(items) :
	if not items :
		print("Cart is empty!")
		return 
	print("--- BILL ---")
	subTotal = 0
	for item in items :
		print(f"{item['name']}	x{item['quantity']}   = {item['price'] * item['quantity']}")
		subTotal += item["price"] * item["quantity"]
	print(f"Subtotal   :    RS.{subTotal}")
	discount = subTotal * 0.1
	print(f"Discount   :    RS.{discount}")
	subTotal -= discount
	print(f"Total      :    RS.{subTotal}")
	

def display() :
	print("==== Shopping Cart ====")
	items = []
	while True :
		print("1. Add Item")
		print("2. Remove Item")
		print("3. Show Cart")
		print("4. Show Bill")
		print("5. Exit")
		try :
			choice = int(input("Choose: "))
		except ValueError :
			print("invalid choice!")
			continue
		if choice == 1 :
			items = addItem(items)
		elif choice == 2 :
			items = removeItem(items)
		elif choice == 3 :
			showCart(items)
		elif choice == 4 :
			bill(items)
		elif choice == 5 :
			print("GoodBye!")
			break
		else :
			print("Enter choice b/w 1-5: ") 

	
	
display()
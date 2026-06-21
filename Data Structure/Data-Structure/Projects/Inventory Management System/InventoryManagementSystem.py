def addProduct(products) :
	name = input("Enter product name: ")
	id = input("Enter product id: ")
	for product in products :
		if id == product['id'] :
			print(f"product with id {product['id']} already exists!\n")
			return products
	product = {}
	while True :
	
		try :
			price = float(input("Enter price: "))

		except ValueError :
			print("price must be in number!")
			continue

		if price < 0 :
			print("price must be positive!")
			continue
		break
	while True :
		
		try :
			quantity = int(input("Enter stock quantity: "))
		except ValueError :
			print("stock quantity must be in number!")
			continue
		if quantity < 0 :
			print("stock quantity must be positive!")
			continue
		break
	
	
	product['name'] = name
	product['id'] = id
	product['price'] = price
	product['stock'] = quantity
	
	products.append(product)
	
	print(f"{name} added successfully!\n")

	return products

def updateStock(products) :
	if not products :
		print("Empty Inventory!")
		return products
	
	Pid = input("Enter Product Id: ")
	
	for product in range(len(products)) :
		if products[product]['id'] == Pid :
			while True :
				try :
					newStock = int(input("Enter new stock quantity: "))

				except ValueError :
	
					print("invalid, stock must be in number!")
					continue
				if newStock < 0 :
					print("stock must be positive!")
					continue
				break
			products[product]['stock'] = newStock
			print(f"{products[product]['name']} stock updated to {newStock}!\n")
			return products

	print(f"{Pid} is not in inventory!\n")
	return products

def searchProduct(products) :
	if not products :
		print("Empty Product Inventory!")
		return 
	prod = input("Enter product name or id: ")
	foundProd = {}

	for product in products :
		if product['id'] == prod or product['name'].lower() == prod.lower() :
			foundProd = product
			break
	if not foundProd :
		print(f"{prod} is not in Inventory!")
		return 
	print("--- Search Result ---")
	
	print(f"ID {' ' * (8 - (len('ID')))} : {foundProd['id']}")
	print(f"{'Name' : < 8} : {foundProd['name']}")
	print(f"{'Stock' : < 8} : {foundProd['stock']}")
	print(f"{'Price' : < 8} : Rs.{foundProd['price']}")
	print(f"{'Value' : < 8} : Rs.{foundProd['price'] * foundProd['stock']}\n")

def lowStockAlert(products) :
	if not products :
		print("Empty product inventory!")
		return
	lowStock = [prod for prod in products if prod['stock'] < 5]
	
	print("--- Low Stock Alert (less than 5) ---")
	if not lowStock :
		print("No product in low stock!")
		return 
	for prod in lowStock :
		print(f"{prod['id'] : < 8}{prod['name'] : < 8}{prod['stock'] : < 8} Rs.{prod['price'] : < 8} ⚠  Low Stock!\n")
	

def inventoryValue(products) :
	if not products :
		print("Empty product inventory!\n")
		return
	print("--- Inventory Value ---")
	total = 0
	for prod in products :
		print(f"{prod['id'] :<8}{prod['name']:<14}Rs.{prod['stock'] * prod['price']}")
	
		total += prod['stock'] * prod['price']
	print(f"{'Total Inventory Value' : <22} : Rs.{total}\n")

def showProducts(products) :
	if not products :
		print("Empty product inventory!")
		return 
	print("--- All Products ---")
	print(f"{'ID' :<8} {'Name':<14}{'Stock' : <8}{'Price' : <8}Value")
	for p in products :
		print(f"{p['id'] : <8}{p['name'] : <14}{p['stock'] : <8}{p['price'] : <8}Rs.{p['stock'] * p['price']}")
	
	print()

def main() :
	print("=== Inventory Management System ===")
	

	products = []
	while True :
		print("""1. Add Product\n2. Update Stock\n3. Search Product
4. Show Low Stock\n5. Show Total Inventory Value\n6. Show All Products\n7. Exit""")

		while True :
			try :
				choose = int(input("Choose: "))
		
			except ValueError :
				print("Invalid, choose must be number!")
				continue
			if choose < 1 or choose > 7 :
				print("choose b/w 1-7!")
				continue
	
			break
	
		match choose :
	
			case 1 :
			
				products = addProduct(products)

			case 2 :

				products = updateStock(products)

			case 3 :
			
				searchProduct(products)

			case 4 :
			
				lowStockAlert(products)
	
			case 5 :
	
				inventoryValue(products)

			case 6 :
	
				showProducts(products)
			
			case 7 :
		
				print("Goodbye!")
				break
		
main()	
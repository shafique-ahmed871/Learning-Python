def addContact(lis) :
	contact = {}
	while True :
		duplicate = False
		name = input("Enter name :")
		phone = input("Enter phone :")
		email = input("Enter Email :")

		contact["name"] = name
		contact["phone"] = phone
		contact["email"] = email
		
		for con in lis :
			if con["phone"] == phone or con["email"] == email :
				if con["phone"] == phone :
					print(phone , "phone number already exists in contacts")
					duplicate = True
					break
				elif con["email"] == email :
					print(email , "email already exits in contacts")
					duplicate = True
					break
					
		if not duplicate :
			lis.append(contact)
		
			print("contact Saved successfully!")
		more = True
		while True :
			again = input("do you want to add more contacts(yes/no) :")
			if again == "yes" or again == "no" :
				if again == "no" :
					more = False
					break
				else :
					more = True
			else :	
				print("only enter yes/no!")
		if not more :
			break
			
	return lis


def searchContact(lis) :
		name = input("Enter conctact name:")
		isFound = False
		for con in lis:
			if con["name"].lower() == name.lower() :
				isFound = True
				print(con["name"] , "|" , con["phone"] , "|" , con["email"])
		if not isFound :
			print("Not found in contact!")

def updateContact(lis) :
	name = input("Enter name to be update:")
	isFound = False
	found = []

	for con in lis :
		if con["name"].lower() == name.lower() :
			
			phone = input("update phone :")
			con["phone"] = phone
			email = input("update email :")
			con["email"] = email
			isFound = True
	if not isFound :
		print(f"no contact exits name {name}")
	else :
		print("contact updated successfully")
	return lis
			
			

def deleteContact(lis) :
	name = input("Enter name to delete:")
	isFound = False
	for con in lis :
		if con["name"].lower() == name.lower() :
			isFound = True
			lis.remove(con)
	if isFound :
		print("contact Successfully deleted!")
	else :
		print("contact is not in phone!")
	return lis

def showAllContact(lis) :
	yes = False
	print("All contacts!")
	for con in lis :
		print(con["name"] , "|" , con["phone"] , "|" , con["email"])
		yes = True

	if not yes :
		print("no contact saved yet!")


def display() :
	print("=== Contact Book ===")
	lis = []
	
	while True :
		
		print("1. Add Contact")
		print("2. Search Contact")
		print("3. Update Contact")
		print("4. Delete Contact")
		print("5. Show All Contacts")
		print("6. Exit")
		try :
			ch = int(input("Choose Option: "))
		
			if ch == 1 :
				lis = addContact(lis)
			elif ch == 2 :
				searchContact(lis)
			elif ch == 3 :
				lis = updateContact(lis)
			elif ch == 4 :
	
				lis = deleteContact(lis)

			elif ch == 5 :
				showAllContact(lis)
			elif ch == 6 :
				print("GoodBye!")
				break
			else :
				print("enter choice b/w 1-6: ")
				continue
		except ValueError :
			print("Enter valid choice!")

display()
	
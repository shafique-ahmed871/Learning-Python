def deleteNumber(contacts) :
	while True :
		phone = input("Enter phone: ")
		for cont in contacts :
			if cont["phone"] == phone :
				print(f"{cont['name']} is removed!")
				contacts.remove(cont)
				return contacts
		print("wrong number, try again!")	
def addContact(contacts) :
	contact = {}
	name = input("Enter name: ")
	phone = input("Enter Phone: ")
	duplicate = False
	for cont in contacts :
		if cont["phone"] == phone :
			duplicate = True
			break
	if duplicate :
		print(f"{phone} is already exists!")
		return contacts
	contact["name"] = name
	contact["phone"] = phone
	contacts.append(contact)
	print("contact saved!")
	return contacts
	
def searchContact(contacts) :
	name = input("Enter name: ").lower()
	isAvail = False
	for contact in contacts :
		if contact["name"].lower() == name :
			print(f"{contact['name']} - {contact['phone']}")
			isAvail = True
	if not isAvail :
		print("Not in a contact!")
	
def deleteContact(contacts) :
	name = input("Enter name: ").lower()
	index = -1
	cont1 = 0
	while cont1 < len(contacts) :
		if contacts[cont1]["name"].lower() == name :
			cont2 = cont1 + 1
			while cont2 < len(contacts):
				if contacts[cont1]["name"] == contacts[cont2]["name"] :
					print(f" more than one contact with name {name}")
					return deleteNumber(contacts)
				cont2 += 1
			index = cont1

		cont1 += 1
	if index == -1 :
		print(f"{name} is not in contact!")
		return contacts
	contacts.remove(contacts[index])
	print(f"{contact[index].['name']} deleted!")
	return contacts

def showContacts(contacts) :
	if not contacts :
		print("Empty contacts book!")
		return 
	print("--- contact Book --- ")
	for contact in contacts :
		print(f"{contact['name']} - {contact['phone']}")



def display() :
	contacts = []
	
	while True :
		print("""1. Add Contact
		2. Search Contact
		3. Delete Contact
		4. Show All
		5. Exit""") 

		try :
			choose = int(input("Choose: "))
		except ValueError :
			print("Invalid choose , must be number:")
			continue
		if choose == 1 :
			contacts = addContact(contacts)
		elif choose == 2 :
			searchContact(contacts)
		elif choose == 3 :
			contacts = deleteContact(contacts)
		elif choose == 4 :
			showContacts(contacts)
		elif choose == 5 :
			print("Goodbye!")
			break
		else :
			print("choose b/w 1-5: ")

display()
		
	
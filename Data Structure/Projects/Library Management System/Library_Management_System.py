def addBook(library) :
	
	book_title = input("Enter book title: ")

	author_name = input("Enter author name: ")

	book_id = input("Enter book id: ")

	if book_id in library.keys() :
		print(f"Book with id {book_id} already in library!")
		return library

	for key , value in library.items() :
		
		if value['Title'] == book_title :

			print(f"{book_title} is already in library!")
		
			return library
		
	book_details = {}
	
	book_details['Title'] = book_title

	book_details['Author'] = author_name

	book_details['Status'] = 'Available'

	library[book_id] = book_details

	print(f"{book_title} added successfully!")

	return library


def issueBook(library) :
	
	if not library :

		print("Empty library!")
	
		return library
	
	book_id = input("Enter book id: ")
	 
	if book_id not in library :

		print(f"Book with id {book_id} is not in library!")
	
		return library

	if library[book_id]['Status'].lower() != 'available' :

		print(f"book with id {book_id} already issued!")

		return library

	student_name = input("Enter student name: ")

	student_id = input("Enter student id: ")

	library[book_id]['Status'] = "issued"
	
	print(f"{library[book_id]['Title']} is issued to {student_name}!")

	return library
		

	
def returnBook(library) :

	if not library :

		print("Empty library!")

		return library

	book_id = input("Enter book id: ")

	isAvail = False

	if book_id in library.keys() :
	
		isAvail = True
	
		if not (library[book_id]['Status'] == 'Available')  :

			library[book_id]['Status'] = 'Available'

			print(f"{library[book_id]['Title']} returned successfully!")
			
			return library
		else :

			print(f"{library[book_id]['Title']} is not issued yet!")

			return library

	if not isAvail :
	
	 	print(f"book with id {book_id} is not in library!")

	return library

def searchBook(library) :

	if not library :
		print(f"Empty library!")

		return 

	print("--- Search Result ---")

	titleOrAuthor = input("Enter title or author to search: ").lower()

	isAvail = False

	for key , value in library.items() :

		if titleOrAuthor in value['Title'].lower() or titleOrAuthor in value['Author'].lower() :
		
			print(f"{key :<8}{value['Title'] :<8}{value['Author'] :<8}{value['Status']}")

		 
			isAvail = True

	if not isAvail :
	
		print(f"{titleOrAuthor} is not in library!")
	
		

def showAvailableBooks(library) :

	if not library :

		print("Empty library!")

	
	available_books= {key : value for key , value in library.items() if value['Status'].lower() == 'Available'.lower()}

	
	print("--- Available Books ---")
	if not available_books :

		print("No book is available currently!")
		return 

	for key , value in available_books.items() :
	
		print(f"{key :<8}{value['Title'] :<8}{value['Author'] :<8}{value['Status']}")

	



def showAllBooks(library) : 

	if not library :

		print("Empty Library!")
		return

	for key , value in library.items() :

		print(f"{key :<8}{value['Title'] :<8}{value['Author'] :<8}{value['Status']}")

		
		 
		

def Menu() :
	
	print("=== Library Book System ===")

	library = {}

	while True :

		print("""1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Book
5. Show Available Books\n6. Show All Books\n7. Exit""")


		while True :
			try :
				choose = int(input("Choose: "))

			except ValueError:

				print("choose must be in number!")
				continue

			if choose < 1 or choose > 7 :
				print("choose must be b/w 1-7: ")
				continue

			break

		match choose :

			case 1 :
				library = addBook(library)

			case 2 :
	
				library = issueBook(library)

			case 3 :

				library = returnBook(library)

			case 4 :

				searchBook(library)

			case 5 :

				showAvailableBooks(library)

			case 6 :

				showAllBooks(library)

			case 7 :
	
				print("Goodbye!")

				break



Menu()


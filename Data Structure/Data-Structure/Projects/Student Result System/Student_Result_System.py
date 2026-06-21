def addStudent(students) :
	name = input("Enter student name: ")
	id = input("Enter student id: ")
	student = {}
	for student_previous in students :
		if student_previous['id'] == id :
			print(f"student with {id} already exists!")
			return students
	
	student['name'] = name
	student['id'] = id
	marks = []
	sum = 0
	for i in range(1 , 6) :
		while True :
			try :
				mark = float(input(f"Enter marks for subject {i}: "))
			except ValueError :
				print("Invalid marks, must be number!")
				continue
			if mark < 0 or mark > 100 :
				print("marks must be b/w (1-100)!")
				continue
			marks.append(mark)
			sum += mark
			break
	
	student['marks'] = marks
	student['total'] = sum
	
	try :
		percentage = sum/len(marks)
	except ZeroDivisionError :
		print("division by zero is undefined")
		return students
	student['percentage'] = percentage
	
	if percentage >= 90 :
		gpa = 4.0
	elif percentage >= 80 :
		gpa = 3.5
	elif percentage >= 70 :
		gpa = 3.0
	elif percentage >= 60 :
		gpa = 2.5
	elif percentage >= 50 :
		gpa = 2.0
	else :
		gpa = 1.5

	student['gpa'] = gpa
	
	if percentage >= 50 :
		student['status'] = 'Pass'
	else :
		student['status'] = 'Fail'
	students.append(student)
	print(f"student {name} added successfully!")
	return students	
	


def showAll(students) :
	print("--- All Results ---")
	if not students :
		print("Empty students result!")
		return 0
	def space(var): 
		return ' ' * (12 - len(var))

	print(f"Name{space('name')}Id{space('id')}Total{space('total')}Percentage{space('percentage')}GPA	Status")
	for student in students :
		name = student['name']
		total = f"{student['total']}/{500}"
		per = f"{student['percentage']:.1f}%"
		gpa = student['gpa']
		status = student['status']
		id = student['id']
		print(f"{name}{space(name)}{id} {space(id)}{total}{space(total)}{per}{space(per)}{gpa}	{status}")

def failedStudent(students) :
	print("--- Failed Students ---")
	found = False
	if not students :
		print("Result card is empty!")
		return 

	for student in students :
		if student['percentage'] >= 50 :
			continue
		print(f"{student['name']}{' ' * (15 - len(student['name']))}{student['total']}/500  {student['percentage']:.1f}%  {student['status']}")
		found = True
	if not found :
		print("Bravo!, all students are passed")
		
def showRanking(students) :
	print("--- Rankings ---")
	if not students :
		print("Empty students' result!")
		return
	if len(students) < 3 :
		print(f"only {len(students)} in result card, must be atleast 3 students!")
		return 
	ranking = findRanking(students)
	pos = 1
	for i in ranking :
		
		print(f"Rank {pos} : {i['name']}{' ' * (12 - len(i['name']))}{i['percentage']:.1f}%")
		pos += 1
def findRanking(students):
    return sorted(students, key=lambda s: s['percentage'], reverse=True)[:3]	

def summarry(students) :
	print("---Class Summarry ---")
	if not students :
		print("Empty student result card!")
		return
	passed = fail = sum = 0
	low = high = students[0]
	total = 5 * len(students)
	for student in students :
		sum += student['total']
		if student['percentage'] >= 50:
			passed += 1
		else :
			fail += 1
		if student['total'] > high['total'] :
			high = student
		if low['total'] > student['total'] :
			low = student
		
	print(f"""Total Students\t: {len(students)}\nPassed\t\t: {passed}
Failed\t\t: {fail}\nClass Average	: {sum/(total):.1f}%
Highest Score	: {high['name']}  {high['percentage']:.1f}%
Lowest Score	: {low['name']}  {low['percentage']:.1f}%""")


def studentResult() :
	print("=== Student Result System ===")
	students = []
	while True :
		print("""1. Add Student\n2. Show All Results
3. Show Rankings\n4. Show Failed Students
5. Show Class Summarry\n6. Exit""")
		try :
			choose = int(input("Choose: "))
		except ValueError :
			print("Invalid choose, must be number!")
			continue
		if choose < 1 or choose > 6 :
			print("Choose must be b/w (1-6)")
			continue
		match choose :
			case 1 :
				students = addStudent(students)
				
			case 2 :
				showAll(students)
			case 3 :
				showRanking(students)
			case 4 :
				failedStudent(students)
			case 5 :
				summarry(students)
			case 6 :
				print("Goodbye!")
				break

	
studentResult()
		
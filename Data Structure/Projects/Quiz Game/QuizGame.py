def attemptQuiz() :
	answers = []
	questions = [
	{
        "question": "What keyword is used to define a function in Python?",
        "options": ["1. func", "2. def", "3. define", "4. function"],
        "answer": 2},
	{
        "question": "Which data type is immutable in Python?",
        "options": ["1. List", "2. Dictionary", "3. Set", "4. Tuple"],
        "answer": 4},
	{
        "question": "What is the output of: print(10 // 3)?",
        "options": ["1. 3.33", "2. 3", "3. 4", "4. Error"],
        "answer": 2},
	{
        "question": "Which method adds an item to the end of a list?",
        "options": ["1. add()", "2. insert()", "3. append()", "4. push()"],
        "answer": 3},
	{
        "question": "What does len() function return?",
        "options": ["1. Last element", "2. First element", "3. Sum of elements", "4. Number of elements"],
        "answer": 4},
	{
        "question": "Which symbol is used for single line comment in Python?",
        "options": ["1. //", "2. /*", "3. #", "4. --"],
        "answer": 3},
	{
        "question": "What is the correct way to create a dictionary in Python?",
        "options": ["1. d = []", "2. d = ()", "3. d = {}", "4. d = <>"],
        "answer": 3},
	{
        "question": "Which loop is used when number of iterations is unknown?",
        "options": ["1. for loop", "2. while loop", "3. do-while loop", "4. foreach loop"],
        "answer": 2},
	{
        "question": "What is the output of: print(type(10.5))?",
        "options": ["1. int", "2. double", "3. number", "4. float"],
        "answer": 4},
	{
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["1. catch", "2. error", "3. except", "4. handle"],
        "answer": 3},
	]
	ques = 0
	print("=== Quiz Game ===")
	for question in questions :
		ques += 1
		while True :
			print(f"Q{ques}: {question['question']}")
			for option in question['options'] :
				print(option)
			try :
				ans = int(input("Your answer: "))
			except ValueError :
				print("invalid, answer in numbers!")
				continue
			if ans <1 or ans > 4 :
				print("answer must be b/w 1-4!")
				continue
			if question['answer'] == ans :
				answers.append(True)
			else :
				answers.append(False)
			break
	print("\n\n")
	print("--- Result ---")
	correct = 0
	for ans in answers :
		if ans :
			correct += 1
	print(f"Score{' ' * (10 - len('Score'))} : {correct}/{len(answers)}")
	percentage = correct * 100 / len(answers)
	print(f"Percentage{' ' * (10 - len('Percentage'))} : {percentage:.1f}%")
	if percentage >= 90:
    		Grade = 'A+'
	elif percentage >= 80:
    		Grade = 'A'
	elif percentage >= 70:
    		Grade = 'B'
	elif percentage >= 60:
    		Grade = 'C'
	else:
    		Grade = 'F'
	print(f"Grade{' ' * (10 - len('Score'))} : {Grade}")
	print("Well done!")

attemptQuiz()

		

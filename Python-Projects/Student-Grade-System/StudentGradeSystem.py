def CalculateGrade() :
	sub = 5

	total = sub * 100

	obtain = 0
	
	for i in range(1 , sub +1) :
		while True :
				
			try :
				marks = float(input(f"Enter marks for subject {i}:"))
			except ValueError :
				print("please Enter a valid marks")
				continue
			if marks > 100 or marks < 0 :
				print("Enter marks b/w 0 to 100!")
				continue
			obtain += marks
			break
		
	print(f"Total: {obtain}/{total}")
	percentage = obtain * 100 / total
	print(f"Percentage: {percentage:.2f}%")
	if percentage >= 90 :
		print("Grade: A+")
	elif percentage >= 80 :
		print("Grade: A")
	elif percentage >= 70 :
		print("Grade: B")
	elif percentage >= 60 :
		print("Grade: C")
	elif percentage >= 50 :
		print("Grade: D")
	else :
		print("Grade: F")

	if percentage >= 60 :
		print("Result: Pass")
	else :
		print("Result: Fail")

CalculateGrade()


		
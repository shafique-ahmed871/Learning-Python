def calculator() :
	num1 = float(input("Enter first number :"))
	operator = input("Enter operator(+ , - , * , /):")
	num2 = float(input("Enter second number :"))

	if operator == "+" :
		return num1 + num2
	elif operator == "-" :
		return num1 - num2
	elif operator == "*" :
		return num1 * num2
	elif operator == "/" :
		if num2 == 0 :
			return "division by zero is undefined"
		else :
			return num1/num2
	else :
		return "invalid Operation"

while True :

	print("Result:" , calculator())
	
	again = input("Calculate again? (yes/no):")
	if again.lower() == "no" :
		print("Goodbye!")
		break


	
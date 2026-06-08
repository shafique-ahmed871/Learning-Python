num = int(input("Enter any number:"))

if( num < 0 and num % 2 == 0) :
	print(num,"is negative Even")
elif(num > 0 and num % 2 == 0) :
	print(num, "is positive even")
elif(num < 0 and num % 2 != 0) :
	print(num, "is negative odd")
elif(num > 0 and num % 2 != 0) :
	print(num, "is positive odd")
else:
	print(num, "is zero")

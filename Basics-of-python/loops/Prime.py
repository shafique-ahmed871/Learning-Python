num = int(input("Enter any number :"))

if num > 1 :if isPrime :
		print(num , "is prime number!")

	isPrime = True
	for i in range(2, num) :
		if(num % i) == 0 :
			isPrime = False
			break
	if isPrime :
		print(num , "is prime number!")
	else :
		print(num , "is not a prime number!")
else :
	print(num , "is not a prime number!")
	

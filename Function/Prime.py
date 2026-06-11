def isPrime(num) :
	if num >= 2 :
		for i in range(2 , int(num ** 0.5)) :
			if num % i == 0 :
				return False
		return True
	return False

num = int(input("Enter any number :"))
print(num , "is prime number:" , isPrime(num))

			
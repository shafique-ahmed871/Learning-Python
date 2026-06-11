ran = int(input("Enter range : "))

for i in range(2, ran + 1) :
	isPrime = True
	for j in range(2, i+1) : 
		if ( i % j == 0) :
			isPrime = False
			break
	if isPrime :
		print(i , end = " ")
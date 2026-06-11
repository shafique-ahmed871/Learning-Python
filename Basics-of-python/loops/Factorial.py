num = int(input("Enter any number :"))

fac = 1

if(num >= 0) :
	print(num,"!", end = " = ")
	fac = 1
	for i in range(num) :
		print(num - i, end = " ")
		if(i != num - 1) :
			print("X", end = " ")
		fac *= (i + 1)
	print(" = ", fac)
else :
	print("negatice number has no factorial")
	
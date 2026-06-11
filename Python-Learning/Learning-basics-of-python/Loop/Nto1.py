n = int(input("Enter any number : "))
sum = 0

for i in range(1 , n+1) :
	print(i,end = " ")
	if(i != n) : 
		print("+",end = " ")
		sum += i

print(" = ",sum)

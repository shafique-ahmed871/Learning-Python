num = int(input("Enter any number :"))
sumEven = 0
print("Even numbers :" , end = " ")
for i in range(1, num + 1) :
	if(i % 2 == 0) :
		print(i , end = " ")
		sumEven += i

print()
print("odd numbers :" , end = " ")
for i in range(1 , num + 1) :
	if(i % 2 != 0) :
		print(i , end = " ")
print()

print("Sum of even numbers :", sumEven)

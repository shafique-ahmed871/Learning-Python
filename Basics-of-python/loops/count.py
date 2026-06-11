num = int(input("Enter any number :"))
count = 0
num2 = num
while num !=  0:
	count += 1
	num //= 10
	
print(num2, "-->",count)
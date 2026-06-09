num1 = int(input("Enter any number:"))
num2 = int(input("Enter any number:"))

if(num1 > num2) :
	print(num1,">",num2)
else :
	print(num1, "<" , num2)



if(num1 % 5 == 0 and num2 % 5 == 0):
	print(num1, "and",num2, "are divisibe by 5")
elif( num1 % 5 == 0 and num2 % 5 != 0) :
	print("only", num1, "is divisible by 5")
elif( num1 % 5 != 0 and num2 % 5 == 0) :
	print("only", num2, "is divisible by 5")
else :
	print(num1 , "and", num2, "both are not divisible by 5")

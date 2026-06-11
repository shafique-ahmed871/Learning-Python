def reverse(num) :
	abs(num)
	r = len(str(num))
	num = int(num)
	reverse = 0
	for i in range(0,r) :
		rem = int(num % 10)
		num = int(num / 10)
		reverse += rem * (10 ** (r - i - 1))
		
	return int(reverse)

num = int(input("Enter any number :"))

print(num , "-->" , reverse(num))
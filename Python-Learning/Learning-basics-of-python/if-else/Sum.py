num = int(input("Enter any number : "))
r = num

while True : 	
      if(num < 10 and num > -10) :
	 sum = r % 10
         r %= 10
	 if(r < 10 and r > -10):

      else :
        sum += r
        break

print("Sum of digit of", num , "is", sum)
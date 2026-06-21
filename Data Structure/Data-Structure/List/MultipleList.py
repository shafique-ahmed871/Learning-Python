li1 = [1 , 2 , 3 , 4]

li2 = ["Shafique" , "Mazhar" , "Kamran"]

li3 = [300 , 230 , 200 , 400]

import itertools

for i , j , k in zip(li1 , li2 , li3) :
	print(i , j , k)

cms = ["0101" , "0051" , "0060" , "0102"]

name = ["Shafique" , "Kamran" , "Mazhar" , "shewa"]

cgpa = [3.29 , 2.9 , 3.51 , 2.5]

for c , n , g in zip(cms , name , cgpa) :
	print(c , n ,g)

print("Now using zip longest")

for c , n , g in itertools.zip_longest(cms , name , cgpa) :
	print(c , n , g)

for i , j , k in itertools.zip_longest(li1 , li2 , li3) :
	print(i , j , k)

print("now using fillvalue")

for c , n , g in itertools.zip_longest(cms , name , cgpa , fillvalue = "Shewa") :
	print(c , n , g)

# using enumerate 

print("using enumerate functin")

for i , val in enumerate(cms) :
	print(val , name[i] , cgpa[i])

# using expression with zip

print("using expression in zip")

for i , j ,k in zip((1 , 2 , 3) , ("Ali" , "Khan" , "ahmed") , (3.0 , 4.0 , 3.5 , 2.5)) :
	print(i , j , k)




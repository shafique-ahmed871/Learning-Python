# importing library itertools

from itertools import chain
nesList = [[3 , 4] , [12.4 , 9.0] , ["hi" , "ok"]]

# using nested for loop

print("using nested for loop")

for x in nesList :
	for y in x :
		print(y , end = " ")
	print()


# using while loop

print("using while loop")

i = 0 
while i < len(nesList) :
	j = 0
	while j < len(nesList[i]) :
		print(j , end = " ")
		j += 1
	print()
	i += 1


# using enumerate 

print("using enumerate ")

for x , y in enumerate(nesList , start = 1) :
	print(f"Group {x} : {y}")
	for a , b in enumerate(y , start = 1):
		print(b , end = " ")
	print()

# using List comprehsion

print("using list comprehsion")

[print(j) for i in nesList for j in i]

# using chain 

print("using chain from itertools")

new = list(chain(*nesList))

print(new)
li = [34 , "hi" , False , 3.13]

# using for loop 
print("using for loop")
for i in li :
	print(i)


# using while loop 
print("using while loop")

i = 0

while i < len(li) :
	print(li[i])
	i += 1

# using enumarate 
print("using enumarate")
for i , val in enumerate(li) :
	print(i , val)

# using for range

print("using for range")

for i in range(len(li)) :
	print(li[i])

# using list comprension

print("using list comprehnsion")

[print(x) for x in li]



student = ["Shafique" , "0101" , 3.29 , 2]

# using for loop 

print("using for loop")

for x in student :
	print(x , end = " ")

print()

# using while loop 

print("using while loop")

i = 0

while i < len(student) :
	print(student[i])
	i += 1

# using enumerate 

print("using enumerate function")

for i , x in enumerate(student) :
	print(i , x)

# using for range function 

print("using for range")

for x in range(len(student)) :
	print(student[x])

# using list comprehsion

print("using list comprehsion")

[print(x) for x in student]




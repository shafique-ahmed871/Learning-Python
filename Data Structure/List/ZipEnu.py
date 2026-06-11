names = ["Shafique" , "Ali" , "Mazhar" , "kamran"]
ages = [19 , 20 , 20 , 21]

for i , (name , age) in enumerate(zip(names , ages) , start = 1) :
	print(i , name , age)

for i , info in enumerate(zip(names , ages) , start = 1) :
	print(i , info)

skills = ["ai" , "db" , "coder"]


for i , (name , age , skill) in enumerate(zip(names , ages , skills)) :

	print(i , name , age , skill)
	print(i , (name , age , skill))

for i , info in enumerate(zip(names , ages , skills)) :
	print(i , info[0] , info[1] , info[2])

print("using cycle method")
import itertools
for i , info in enumerate(zip(names , ages , itertools.cycle(skills))) :
	print(i , info)

print("using zip longest")

res = list(itertools.zip_longest(names , ages , skills , fillvalue = 'AI'))

print(res)

print("using enumerate and modulo")

ta = []

for i , item in enumerate(names) :

	ta.append((item , skills[i%len(skills)]))

print(ta)


newli = [(name , skill if skill else "coder") for name , skill in zip(names , skills)]

print(newli)



number = [3 , 5, 3, 6, 35, 63 , 34]

string = ["ali", "ahmed" , "pure" , "sweet"]

decimal = [35.3 , 34.9 , 63.4 , 34.90]

cond = [True , False , False , True , False]

num = list((35 , 34 , 34, 63, 34))

st = list(("hi" , "hello" , "ok"))

dec = list((34.3 , 3.9 , 14.7))

con = list((True , False , True))

a = ["Shafique"] * 5

b = [34] * 3


print("Simple list :" , number)

print("indexing list")
print(number[0])
print(number[-3])

number.append(25)
number.append(17)

print("after append:" , number)

number.remove(25)
number.remove(17)

print("after remove:" , number)

number.insert(0 , 12)
number.insert(2 , 30)

print("after insert:" , number)

number.extend((23, 0 , 8))

print("after extend:" , number)

number[2] = 24

print("After updates:" , number)

number.pop()

print("after pop:" , number)

number.pop(2)

print("after indexed pop:" , number)

del number[0]

print("after del:" , number)

print("iterating over list:")

for i in number:
	print(i , end = " ")


number.clear()

print("after clear:" , number)
# print(string)


# multilist

li = [[34, 34, 3] , ["hi" , "hello" , "ok"]]

print(li[1][1])


# print(decimal)

# print(cond)

# print(num)

# print(st)

# print(dec)

# print(con)

# print(a)

# print(b)
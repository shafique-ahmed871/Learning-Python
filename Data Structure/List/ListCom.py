num = [1 , 2 , 3 , 4 , 5, 6 , 8]

li = [x ** 2 for x in num]

print(li)


even = [ x for x in num if x % 2 == 0]

print(even)

lis = [ x for x in range(10)]

print(lis)

nest = [x **y for x in range(1 , 5) for y in range(1,4)]

print(nest)

nestList = [[2 , 6 , 3 , 10] , [0 , 8 , 5]]

line = [y for x in nestList for y in x]

print(line)
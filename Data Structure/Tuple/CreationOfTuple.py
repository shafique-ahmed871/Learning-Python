tup1 = (2 , 4, 4 ,23, 34,10)

tup2 = (True , False , False , True)

tup3 = (12.4 , 11.9 , 8.4 , 9.0)

tup4 = ("Kami" , "Shafi" , "mazi")

tup5 = (True , 34 , 12.0 , "Shafique")

print(tup1)
print(tup2)

print(tup3)
print(tup4)

print(tup5)

tuple1 = tuple("happy end")

print(tuple1)

tup = (23 , True , 3.03 , [34 , "hi" , True] , {"name" : "Shafique"} , "done")

print(tup)

print(tup1[0])
print(tup1[:4])
print(tup1[1:])
print(tup1[::-1])
print(tup1[-4:-1])

a , *b, c = tup1

print(a)
print(b)
print(c)

print(tup1 + tup2)
from collections import namedtuple

tup = namedtuple("tup" , ["x" , "y"])

p = tup(4 , 9)

print(p)
print(p[0])
print(p.x)


from collections import namedtuple

nt = namedtuple("nt" , ["name" , "age"])

shafi = nt("Shafique" , "19")

kami = nt("Kamran" , "21")

print(shafi)

print(shafi[0])

print(shafi.age)

print(kami)

print(kami.name)

print(kami[1])


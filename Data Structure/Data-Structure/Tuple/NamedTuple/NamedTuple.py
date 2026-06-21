from collections import namedtuple

nameTup = namedtuple("nameTup" , ["name" , "age" , "cgpa"])

s = nameTup("Shafique" , "20" , 3.29)

k = nameTup("Kamran" , "21" , 3.8)

print(s.name)

print(s[0])
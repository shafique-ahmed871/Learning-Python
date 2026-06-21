from collections import namedtuple

student = namedtuple("student" , ["cms" , "name" , "age"])

s1 = student("0101" , "Shafique" , "19")

li = ["0051" , "Kamran" , "21"]

di = {"cms" : "0060" , "name" : "Mazhar" , "age" : "20"}

print("using _make function")

print(student._make(li))

print(student._make(di))


print(s1._asdict())

print(student(**di))

print(student._fields)

print(s1._replace(name = "Nawab"))

print(student.__new__(student , "0102" , "Shewa" , "20"))

print(s1.__getnewargs__())
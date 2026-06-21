person = {"cnic" : "0101" , "name" : "Shafique" , "age" : "19"}

emp = {"Id" : "E0101" , "name" : "Mazhar" , "roll" : "Manager"  , "salary" : 30000}

print(person)

print(emp)

course = dict(cId = "C01" , cName = "DB")

print(course)

print(person["cnic"])

print(person.get("name"))

print(person.get("salary"))

person["city"] = "Khairpur"

person["cnic"] = "45203"

print(person)

del person["city"]

print(person)

print(emp.pop("Id"))

print(emp.popitem())


print("returning keys")

for key in person :
	print(key)

print("returning values")

for value in person.values() :
	print(value)

print("retuning key and value")

for key , value in person.items() :
	print(key , value)


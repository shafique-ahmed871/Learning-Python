from collections import namedtuple

tup = namedtuple("tup" , ["empId" , "empName"])

emp1 = tup("01" , "Khan")

emp2 = tup("02" , "ali")

print("accessed using indexed:" , end = "")

print(emp1[0] , emp1[1] , end = '\t')

print(emp2[0] , emp2[1])

print("accessed using keyname:" , end = " ")

print(emp1.empId , emp1.empName , end = "\t")

print(emp2.empId , emp2.empName)

print("accessed using getattar:" , end ="")

print(getattr(emp1 , "empId" ))

print(getattr(emp2 ,  "empName"))
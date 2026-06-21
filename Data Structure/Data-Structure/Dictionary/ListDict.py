li = [{"PF" : "C++", "OOP" : "Java", "DSA" : "Python"} ,
	{"Python" : "AI" , "javascript" : "Web development"}]

for i in li :
	for  key , value in i.items() :
		print(f"{key}:{value}" , end = " ")

print()
print("using index")
for i in range(len(li)) :
	for key , value in li[i].items() :
		print(f"{key}:{value}")


print("using key")

for i in li :
	for key in i.keys() :
		print(key)
	
	print("=======")



print(*[key for i in li for key in i.keys()])
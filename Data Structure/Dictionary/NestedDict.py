dic = {"student 1" : {"name" : "Shafique Ahmed" , "age" : "19"} ,
	"student 2" : {"name" : "Kamran Ali" , "age" : "21"}}


for i in dic :
	print(dic[i])

for i in dic:
	print(dic.keys())

for i in dic:
	for i in dic :
		print(dic.values())

for i in dic.keys():
	for k , v in dic[i].items():
		print(k , v)


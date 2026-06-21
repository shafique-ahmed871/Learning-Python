dic_li = {"marks" : [45 , 99] , "names" : ["Ali" , "Ahmed"]}


print("original values")
print(dic_li)

res = [[i for i in dic_li[x]] for x in dic_li.keys()]

print(res)

res = []

print(res)

for i in dic_li.values() :
	res.append(list(map(lambda x : x , i)))

print(res)

res = []

print(res)

import itertools

for key , value in (
		itertools.chain.from_iterable(
		[itertools.product((k ,) , v) for k , v in dic_li.items()])) :
		res.append(value)

print(res)

res = []

print(res)

for i in dic_li.values() :
	res.append([x for x in i])

print(res)
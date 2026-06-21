import operator
li1 = [3 , 4 , 5]
li2 = ["shafique" , "ali" , "khan"]

res = list(zip(li2 , li1))

res.sort(key = lambda x : x[0])

print(res)

sortList = sorted(res , key = operator.itemgetter(0))

print(sortList)

sortList = sorted(res , key = lambda x : x[0])

print(sortList)


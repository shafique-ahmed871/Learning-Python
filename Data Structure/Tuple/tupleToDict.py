lis = [(1 , "hi") , (2 , "ok")]

dic = dict(dict(lis))

print(lis)
print(dic)

dic = {key : value for key , value in lis}

print(lis)
print(dic)

rev = {}

for key , value in lis :
	rev[key] = value

print(lis)
print(rev)

rev = dict(map(lambda x : (x[0] , x[1]) , lis))

print(lis)
print(rev)

print("using dict method")

rev = dict(lis)

print(rev)

print("using dict comprehsion")

rev = {key : value for key , value in lis}

print(rev)

print("usin loop")

rev = {}

for key , value in lis :
	rev[key] = value

print(rev)

print("using map and dic")

rev = dict(map(lambda x : (x[0] , x[1]) , lis))

print(rev)
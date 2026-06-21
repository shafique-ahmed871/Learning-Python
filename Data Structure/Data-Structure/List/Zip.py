vowels = ['a' , 'e' , 'i' , 'o' , 'u']

consonents = ['b' , 'c' , 'd' , 'f']

num = [2 , 4, 3]

from itertools import chain
res = (list(zip(vowels , consonents , num)))

print(res)

print(list(zip()))

print(list(zip(vowels)))

print(list(zip(vowels , consonents)))

a , b , c = zip(*res)

print(a)
print(b)
print(c)

dic = {"name" : "Shafique" , "cms" : "0101"}

print(list(zip(dic.keys() , dic.values())))
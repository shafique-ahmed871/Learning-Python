
import numpy as np

li = [[2 , 5] , [2, 5, 3] , [4, 0]]

lo = [[2 , 5, 3] , [6 , 9 , 10]]

res = [(x , y) for x , y in zip(li , lo)]

print("using list comp")

print(res)

print("using zip longest")

import itertools

rest = list(itertools.zip_longest(li , lo , fillvalue = []))

print(rest)

print("using loop")

newli = []

for i in range(len(lo)) :
	newli.append(li[i] + lo[i])

print(newli)

print("using numpy")


arr = np.array([np.array([x, y]) for x, y in zip(li , lo)])

print(arr)
tup = (23 , True , 34 , "shafi")

rev = tup[::-1]

print("reverse tuple using slicing")

print(rev)

rev = tuple(reversed(tup))

print("tuple reverse using reversed")

print(rev)

print(tup)

rev = tuple(tup[i] for i in range(len(tup) - 1 , -1 , -1))

print(rev)


from collections import deque

rev = deque(tup)

rev.reverse()

revs = tuple(rev)

print(revs)

print(tup)
print("using slicing")
rev = tuple(tup[::-1])
print(rev)

print(tup)
print("using reversed")
rev = tuple(reversed(tup))
print(rev)

print("using loop")
print(tup)

rev =tuple(tup[i] for i in range(len(tup) - 1 , -1 , -1))
print(rev)

print("using collections or deque")
from collections import deque 

deq = deque(tup)

deq.reverse()

rev = tuple(deq)

print(tup)
print(rev)

s1 = {23 , 45 , True , False , "set" , "Operations" , 3.14 , 1.718}

s2 = {45 , 91 , "set" , 3.14 , True , "Method" , 6.84 , True}

print("sets")
print(s1)
print(s2)

s1.add("element")
s2.add("element")
print("after add method")
print(s1)
print(s2)

s1.remove("set")
s2.remove("set")

print("after remove method")
print(s1)
print(s2)

s1.discard(23)
s2.discard(91)

print("after discard method")
print(s1)
print(s2)

a = s1.pop()
b = s1.pop()

print("after pop method")

print(a)
print(s1)
print(b)
print(s2)



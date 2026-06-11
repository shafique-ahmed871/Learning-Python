address = {"city" : "Khairpur" , "postal code" : "12029" , "street" : "Babarloi"}

# iterating through key 

for key in address.keys() :
	print(key , end = " ")

print()

# iterating through values

for value in address.values() :
	print(value , end = " ")

print()

# iterating through key and value

for key , value in address.items() :
	print(f"{key} : {value}")

print()
map_add = map(address.get , address)

for key in map_add :
	print(key , end = " ")
print()

for key , value in zip(address.keys() , address.values()) :
	print(f"{key} : {value}")

key = [*address]

value = "{city}-{postal code}-{street}".format(*address , **address)

print(key)
print(value)

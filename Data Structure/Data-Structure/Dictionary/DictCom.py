num_sq = {x : x**2 for x in range(1 , 11)}

print(num_sq)

even_num_sq = {x : x**2 for x in range(1 , 6) if x**2 % 2 == 0}

print(even_num_sq)

odd_num_cube = {x : x**3 for x in range(1 , 6) if x**3 % 2 != 0}
print(odd_num_cube)

li_key = ["name" , "age" , "salary"]
li_value = ["Shafique" , "20" , 30000.0]

dic = {x : y for (x , y) in zip(li_key , li_value)}

print(dic)

friut_key = ["friut" , "color" , "quantity"]
friut_value = ["Apple" , "red" , 50]

dic = {x : y for (x , y) in zip(friut_key , friut_value)}

print(dic)

bool_value = {x : True for x in range(1 , 5)}

print(bool_value)

dic = {x.lower() : x + "dic" for x in "World"}

print(dic)

names = ["Shafique" , "Mazhar" , "kamran" , "Ali Raza"]

names_dic = {x : len(x) for x in names}

print(names_dic)

dict_key = dict.fromkeys(range(5) , "Shafi")
print(dict_key)

dict_key = dict.fromkeys((i for i in "Hello") , "Jatoi")

print(dict_key)

nest_dic = {x : { x+y for y in "jatoi" } for x in "Hello"}
print(nest_dic)

num = {"n" : 56 , "m" : 90 , "k" : 100}

print(num)

print(num.get("n"))

print(num.values())

print(list(num.items())[1][1])

num.update({"n" : 80 , "m" : 40})
print(num)

num.clear()

print(num)


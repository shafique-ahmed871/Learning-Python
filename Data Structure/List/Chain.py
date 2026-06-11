li1 = [3 , 6, 23 , 5, 0]

li2 = [2.3 , 3.0 , 3.8 , 9.2]

from itertools import chain

li1_li2 = list(chain(li1 , li2))

print(li1_li2)

nest = [[2 , 5, 19 , 14] , [13 , 9 , 10 , 12]]

nestChain = list(chain(*nest))

print(nestChain)

net = list(chain(nest[0] , nest[1]))

print(net)

print(list(chain("abcd" , "dhas" , "dfh")))

print("".join(list(chain("sh" , "af" , "iq" , "ue"))))

print(list(map(int , chain("123843"))))


single = ["ali" , "khan" , "ahmed"]

print("using chain:" , list(chain(single)))

print("using iterable:" , list(chain.from_iterable(single)))





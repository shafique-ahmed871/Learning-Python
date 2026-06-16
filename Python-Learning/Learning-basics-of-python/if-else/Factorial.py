num = int(input("Enter any number : "))
fac = 1
if(num >= 0) :
    if(num == 1 or num == 0) :
       fac = 1
    else :
     for i in range(num):
         fac *= (i + 1)
    print(num,"! = ",fac)
else :
    print("negative number has no factorial!")
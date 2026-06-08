charac = input("Enter any character : ")

if(charac >= "a" and charac <= "z") or (charac >= "A" and charac <= "Z"):
    if(charac in ("a","A", "E","e","i","I","O","o","u","U")) :
      print(charac , "is the vowel!")
    else : 
       print(charac, "is consonent!")
else :
    print("not a character!")
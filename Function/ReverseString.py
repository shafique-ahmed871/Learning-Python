def reverseString(string) :
	reverse = ""
	for i in range(len(string)) :
		reverse += string[len(string) - i -1]
	return reverse

string = input("Enter any string :")

print(string , "-->" , reverseString(string))
def greet() :
	print("Hello, World!")


def printName(name) :
	print("Hello",name)

def sum(num1 , num2) :
	return num1 + num2

def square(num) :
	return num * num

def evenOdd(num) :
	if num % 2 == 0 :
		print(num , "is Even")
	else :
		print(num , "is Odd")

def largest(num1 , num2) : 
	if num1 > num2 :
		print(num1 , "is the largest!")
	else :
		print(num2 , "is the largest!")

def area(width , length) :
	return width * length

def convertor(c) :
	return (9 * c / 5) + 32

def count(word) :
	return len(word)


def factorial(num) :
	if(num >= 0) :
		if num == 0 :
			return 1
		else :
			return num * factorial(num - 1)

	else :
		print("undefined")


greet()

printName("Shafique")

print("sum:", sum(8 , 5))

print("square:", square(5))


evenOdd(17)

largest(12,20)

area(8 , 5)

convertor(58)

count("python")

print(6 , "!=" , factorial(6))

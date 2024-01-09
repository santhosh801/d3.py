
def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


select = int(input("Select operations form 1, 2, 3, 4 :"))

n1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(n1, "+", number_2, "=",
					add(n1, number_2))

elif select == 2:
	print(n1, "-", number_2, "=",
					subtract(n1, number_2))

elif select == 3:
	print(n1, "*", number_2, "=",
					multiply(n1, number_2))

elif select == 4:
	print(n1, "/", number_2, "=",
					divide(n1, number_2))
else:
	print("Invalid input")

def num_div(num1, num2):
	# sol = float(num1) / float(num2)
	# print(sol)
	try:
		x = (float(num1) / float(num2))
	except ZeroDivisionError:
		pass
	else:
		print(x)

a = input('What is your first number? ')
b = input('What is your second number? ')

num_div(a, b)

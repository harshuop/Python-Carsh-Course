def addition(num1, num2):
    try:
        x = int(num1) + int(num2)
    except ValueError:
        print(' Please use numbers')
    else:
        print(x)

n1 = input(' What is your first number: ')
n2 = input('What is your second number: ')

addition(n1, n2)

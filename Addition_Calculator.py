def addition(num1, num2):
    try:
        x = int(num1) + int(num2)
    except ValueError:
        print(' Please use numbers\n')
    else:
        print(' Ans: ' + str(x) + '\n')


while True:
    n1 = input(' What is your first number: ')
    n2 = input('What is your second number: ')

    addition(n1, n2)

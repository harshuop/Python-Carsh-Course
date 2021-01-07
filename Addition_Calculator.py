
def addition(num1, num2):
    try:
        x = int(num1) + int(num2)
    except ValueError:
        print(' Please use numbers')
    else:
        print(x)

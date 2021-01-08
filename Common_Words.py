files = ['LocalFolder/A_Century_of_Parody.txt', 'LocalFolder/The_Venus_Evil.txt']
value = 'the'

try:
    for name in files:
        with open(name) as content:
            text = content.read()
            print('File name: ' + name)
            print(' -Number of values: ' + str(text.lower().count(value)) + '\n')
except FileNotFoundError:
    print('\n' + str(name) + ' not exist\n')
else:
    pass
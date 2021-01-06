name = input('What is your name: ')
file = 'LocalFolder/guest.txt'

with open(file, 'a') as add:
    add.write(name.title() + '\n')

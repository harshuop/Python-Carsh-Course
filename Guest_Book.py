file_name = 'LocalFolder/guest_book.txt'

print(' ENTER "q"  TO QUIT \n\n')
while True:
    name = input('What is your name: ')

    if name.lower() == 'q':
        break
    else:
        with open(file_name, 'a') as area:
            area.write(name + '\n')
        print('Thank You, ' + name + ' for visiting!\n')

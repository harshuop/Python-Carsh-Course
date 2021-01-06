file = 'programming.txt'

with open(file, 'w') as e_file:
    e_file.write('* This line is added by an command...\n')
    e_file.write('* This is another line!\n')

with open(file, 'a') as e_file:
    e_file.write('* This is an post added line!\n')

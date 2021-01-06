file = 'programming.txt'

with open(file, 'w') as e_file:
    e_file.write('* This line is added by an command...')

with open(file, 'w') as e_file:
    e_file.write(
        '* This is another line by the same program '
    )

s_file = 'LocalFolder/programming_pool.txt'

print('ENTER "q" TO QUIT THE PROGRAM\n\n') 
while True:
    reason = input('Why you like programming? ')

    if reason.lower() == 'q':
        with open(s_file, 'a') as enter:
            enter.write('\n') 
        break
    else:
        with open(s_file, 'a') as storage:
            storage.write(reason + '\n')

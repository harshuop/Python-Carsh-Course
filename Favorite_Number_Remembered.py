import json
file_name = 'user_f_num.json'

try:
    with open(file_name) as storage:
        res = json.load(storage)
except FileNotFoundError:
    number = int(input("What is your favorite number: "))
    with open(file_name, "w") as storage:
        json.dump(number, storage)
        print('OK! I will remember that...')
else:
    print('Your favorite number is: ' + str(res))

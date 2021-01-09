import json
file_name = 'user_f_num.json'

def greet():
    with open(file_name) as storage:
        print('Your favorite number is: ' + str(json.load(storage)))

greet()

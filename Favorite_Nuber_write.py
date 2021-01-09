import json
file_name = 'user_names.json'
number = int(input("What is your favorite number: "))

def input_user():
    with open(file_name, "w") as storage:
        json.dump(number, storage)
        print('OK! I will remember that...')

input_user()

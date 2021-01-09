import json
file_name = 'user_names.json'

def stored_name():
    """This will give output for the saved username"""
    try:
        with open(file_name) as storage:
            name = json.load(storage)
    except FileNotFoundError:
        pass
    else:
        return name

def new_user():
    """This will a new user"""
    try:
        name = input('What is your user name: ')
        with open(file_name, "w") as storage:
            json.dump(name, storage)
    except FileNotFoundError:
        pass
    else:
        print('  Thankyou, I will remember you...\n')

def greet_user():
    """Greet the user by name."""
    name = input('Is your name ' + str(stored_name()) + ' (Y/n)')

    if name.lower() == 'y':
        print('Welcome Back! ' + stored_name())

    elif name == 'n':
        new_user()
        greet_user()

greet_user()
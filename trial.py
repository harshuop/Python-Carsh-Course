import json

<<<<<<< HEAD
numbers  = [135,35,235,35,6353,35,"Hello World!"]
file_name = 'numbers.json'

with open(file_name, "w") as nums:
    json.dump(numbers, nums)

with open(file_name) as obj:
    print(json.load(obj))


print()
=======
numbers = [25,6,547,67,6,33,76658,72346,34]
file_name = 'numbers.json'

with open(file_name, "w") as storage:
    json.dump(numbers, storage)

with open(file_name) as storage:
    print(json.load(storage))
>>>>>>> working_branch

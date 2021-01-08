import json

numbers  = [135,35,235,35,6353,35,"Hello World!"]
file_name = 'numbers.json'

with open(file_name, "w") as nums:
    json.dump(numbers, nums)

with open(file_name) as obj:
    print(json.load(obj))


file = 'LocalFolder/junk.txt'


# Reading and printing the entire file
print('\nReading and printing the entire file')
with open(file) as e_file:
    text = e_file.read()
    print(text)

# Looping over the file objects
print('\nLooping over the file objects')
with open(file) as e_file:
    for text in e_file:
        print(text.rstrip())

# Storing line in a list
print('\nStoring line in a list')
with open(file) as e_file:
    txt = e_file.readlines()

for lines in txt:
    print(lines.rstrip())
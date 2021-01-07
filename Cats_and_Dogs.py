filenames = ['LocalFolder/cats.txt', 'LocalFolder/dogs.txt']

def pets(filename):
    try:
        with open(filename) as file:
            names = file.readlines()
    
    except FileNotFoundError:
        print('*' + filename + ' file not found.')
    
    else:
        print('\n *' + filename)
        for name in names:
            print('   -' + name.rstrip())

for files in filenames:
    pets(files)
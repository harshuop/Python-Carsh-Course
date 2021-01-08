filenames = ['LocalFolder/cats.txt', 'LocalFolder/dogs.txt']

def pets(filename):
    """This is an standard doc string"""
    try:
        with open(filename) as file:
            names = file.readlines()
    
    except FileNotFoundError:
        pass
    
    else:
        print('\n *' + filename)
        for name in names:
            print('   -' + name.rstrip())

for files in filenames:
    pets(files)
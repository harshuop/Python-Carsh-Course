class Restaurant:
    """This is a class where we are defining a Restaurant"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name.title().replace('_', ' ')
        self.cuisine_name = cuisine_name.title().replace('_', ' ')
    
    def describe_restaurant(self):
        print('\n')
        print('Name of Restaurant: ' + self.restaurant_name)
        print('Cuisine Type available: ' + self.cuisine_name)
    
    def open_restaurant(self):
        print('\n')
        print('   Restaurant is open today!')


RnK = Restaurant('Radha_Krishn', 'italian_pasta')

RnK.describe_restaurant()
RnK.open_restaurant()
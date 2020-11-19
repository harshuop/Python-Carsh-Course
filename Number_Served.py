class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print("Name of the Restaurant: " + self.name)
        print('Special Cuisine: ' + self.cuisine_type)

    # def open_restaurant(self):
    #     """Display a message that the restaurant is open."""
    #     msg = self.name + " is open. Come on in!"
    #     print("\n" + msg)

    def set_number_served(self, set_number):
        """This will show this default value of hoe many dishes are served today"""
        self.number_served =+ set_number
        print(' The number of dishes served: ' + str(self.number_served))

    def increment_number_served(self, update):
        """This will update the number of dishes served"""
        self.number_served += update
        print('  The number of dishes served: ' + str(self.number_served))


mac = Restaurant(
    'Radha_Krishn',
    'Pizza'
)

mac.describe_restaurant()
mac.set_number_served(2)
mac.increment_number_served(43)
mac.increment_number_served(65)
mac.increment_number_served(35)
mac.increment_number_served(34)

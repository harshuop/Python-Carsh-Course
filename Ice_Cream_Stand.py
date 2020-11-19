class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)


class IceCreamStand(Restaurant):
    """This is is the baby class for the above class"""

    def __init__(self, name, cuisine_type = 'Ice Cream'):
        super().__init__(name, cuisine_type)
        self.flavours = []

    def dis_flav(self):
        """This method will display the flavours output"""

        print('Wecome to our restaurant ' + self.name + '\n our speciality is IceCream.')
        print('We have the following flavours available: ')

        for flav in self.flavours:
            print('  # ' + flav.title())


mac = IceCreamStand('RadhaKrishn')
mac.flavours = ['Vanela', 'Mango', 'Chocolate'] 
mac.dis_flav() 

mac.describe_restaurant()

# Restaurant('Hello', 'Full meal')
# Restaurant.describe_restaurant()z


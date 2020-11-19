class Restaurant():
    """Info of multiple restaurants"""

    def __init__(self, name, s_dish):
        """root information for the program"""
        self.name = name.title()
        self.s_dish = s_dish.title()

    def describe_user(self):
        """This is the small description for the restaurants"""
        print(
            self.name + ' is a very good restaurant.\n ' + self.s_dish + ' is a very good dish of there.'
        )

    def open_status(self):
        """The status of the restaurant that weather the restaurant is open or not"""
        print(
            self.name + ' is open today.\n'
        )


R1 = Restaurant('Mac_D', 'veg_burger')
R1.describe_user()
R1.open_status()

R2 = Restaurant('Subway', 'chicken_roll')
R2.describe_user()
R2.open_status()

R3 = Restaurant('radha_krishn', 'makhan')
R3.describe_user()
R3.open_status()

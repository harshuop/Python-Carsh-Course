class User():
    """User info of a user"""

    def __init__(self, f_name, l_name, location, age, education):
        """root info for this program"""
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.location = location.title()
        self.age = age
        self.education = education

    def describe_user(self):
        """Summary of the user"""
        print('  Hello ' + self.f_name , self.l_name + '!')
        print('Location: ' + self.location)
        print('Age: ' + str(self.age))
        print('Eduction: ' + self.education)

    def greeting(self):
        """A special personalised greeting to the user"""
        print(' ' + self.f_name + '! Thank You, for taking part in the survey.\n')


P1 = User('Harsh', 'wardhan', 'dehradun', 15, 'B.Tech')
P1.describe_user()
P1.greeting()

P2 = User('Abhinandan', 'thakur', 'amritsar', 10, 'Professional Gamer')
P2.describe_user()
P2.greeting()

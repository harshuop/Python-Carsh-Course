class User:
    """User info of a user"""

    def __init__(self, f_name, l_name, location, age, education):
        """root info for this program"""
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.location = location.title()
        self.age = age
        self.education = education
        self.login_attempts = 0

    def describe_user(self):
        """Summary of the user"""
        print(' Hello ' + self.f_name, self.l_name + '!')
        print('Location: ' + self.location)
        print('Age: ' + str(self.age))
        print('Eduction: ' + self.education)

    def increment_login_attempt(self):
        """It will increase the vale of logins"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """This will rest the login all the login attempts"""
        self.login_attempts = 0

    def pr_log(self):
        """This will print the number of logins happen in the account"""
        print(' Number of logins: ' + str(self.login_attempts))

    def greeting(self):
        """A special personalised greeting to the user"""
        print(' ' + self.f_name + '! Thank You, for taking part in the survey.\n')


P1 = User('Harsh', 'wardhan', 'dehradun', 15, 'B.Tech')
# P2 = User('Abhinandan', 'thakur', 'amritsar', 10, 'Professional Gamer')

P1.describe_user()
P1.increment_login_attempt()
P1.increment_login_attempt()
P1.increment_login_attempt()
P1.pr_log()

P1.reset_login_attempts()
P1.pr_log()

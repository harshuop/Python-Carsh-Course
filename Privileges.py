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


class Privileges:
    """This class is only to define the 'privileges' attribute given below"""
    def __init__(self, privileges):
            self.privilege = privileges

    def show_privileges(self):
        """This method will display the display the privileges of the admin"""
        
        print(' Following are the privileges of an admin: ')
        for privilegess in self.privilege:
            print(' - ' + privilegess)


class Admin(User):
    """This is a baby class of the above class, It is being written to give priveliges to the Admin"""

    def __init__(self,  f_name, l_name, location, age, education):
        super().__init__(f_name, l_name, location, age, education)

        self.privilege = Privileges([])
   

mac = Admin('Harshwardhan', 'OP', 'Dehradun', 16, 'In High School')
mac.privilege.privileges = [
    'Can post unlimited posts',
    'No video limit',
    'Can add anyone',
    'Can remove anyone',
    'Can contest any compititions'
]

mac.describe_user()
mac.privilege.show_privileges()

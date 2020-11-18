class Robot:
    """This is a class defining robot"""

    def __init__(self, name, color, weight):
        self.name  = name.title()
        self.color = color 
        self.weight = weight

    def introduceSelf(self):
        print('Name of Robot: ' + self.name)
        print('Color of Robot: ' + self.color)
        print('Weight of Robot: ' + str(self.weight) + ' Kg')


r1 = Robot('Tom', 'red', 30)
r1.introduceSelf()


class RobooT(Robot):
    """This is the baby class of the above class"""
    
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)

print('\n')
r2 = RobooT('Jerry', 'blue', 40)
r2.introduceSelf()
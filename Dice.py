from random import randint

class Die:
    """This is a virtual dice"""

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        n_roll = 0
        print('\nDice of ' + str(self.sides) + ' sides: ')

        while n_roll != 10:
            num = randint(1, self.sides)
            n_roll += 1
            print('Roll' + str(n_roll) + ': ' + str(num))

Die().roll_die()


class Die10(Die):
    """This is the Dice having 10 sides"""

    def __init__(self, sides=10):
        super().__init__(sides)
        self.sides = sides

Die10().roll_die()


class Die20(Die):
    """This is the Dice having 10 sides"""

    def __init__(self, sides=20):
        super().__init__(sides)
        self.sides = sides

Die20().roll_die()
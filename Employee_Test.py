import unittest
from Employee import Employee

class Employee_Test(unittest.TestCase):
    """This is a test to ensure weather Employee.py is working correctly"""
    def setUp(self):
        self.main = Employee('Harsh','Powar',50000)
    def test_give_default_raise(self):
        self.main.give_rise()
        self.assertEqual(self.main.salary, 55000)
    def test_give_custom_raise(self):
        self.main.give_rise(10000)
        self.assertEqual(self.main.salary, 60000)
unittest.main()
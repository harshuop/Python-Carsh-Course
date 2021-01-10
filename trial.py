import unittest

def name_stock(f_name,l_name,m_name=''):
    if m_name:
        name = f_name + ' ' + m_name + ' ' + l_name
    else:
        name = f_name + ' ' + l_name   
    return name.title()

class FirstTest(unittest.TestCase):
    """Checking weather"""
    def test_f_l_name(self):
        check = name_stock('james','jock')
        self.assertEqual(check, 'James Jock')
    def test_f_m_l_name(self):
        check = name_stock('harry', 'loren', 'stacks')
        self.assertEqual(check, 'Harry Stacks Loren')

unittest.main()
import unittest
from city_functions2 import CityCountry

class TestingFile(unittest.TestCase):
    """Testing method CityCountry"""
    def test_city_country(self):
        output = CityCountry('santiago', 'chile', 5000000)
        self.assertEqual(output, 'Santiago Chile 5000000')

unittest.main()

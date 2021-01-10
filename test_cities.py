import unittest
from city_functions import CityCountry

class TestingFile(unittest.TestCase):
    """Testing method CityCountry"""
    def test_city_country(self):
        output = CityCountry('santiago', 'chile')
        self.assertEqual(output, 'Santiago Chile')

unittest.main()

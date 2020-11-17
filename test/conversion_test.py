from unittest import TestCase
from util.conversion import TemperatureKelvin
import logging


class TestTemperatureKelvin(TestCase):
    def setUp(self):
        self.temp_kelvin = TemperatureKelvin(300)

    def test_convert_celsius(self):
        """
        Test conversion kelvin to celsius
        """

        self.assertEqual(26.85, self.temp_kelvin.convert_to_celsius())
from unittest import TestCase
from app import create_app
import logging


class TestWeather(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_weather(self):
        """
        Tests weather endpoint
        """
        params = {
            'City': 'Bogota',
            'Country': 'Co'
        }
        rv = self.app.get('/api/weather', query_string=params)

        # If we recalculate the hash on the block we should get the same result as we have stored
        self.assertEqual(200, rv.status_code)

    def test_weather_params(self):
        """
        Test weather endpoint when params are not set
        """
        rv = self.app.get('/api/weather')
        # If we recalculate the hash on the block we should get the same result as we have stored
        self.assertEqual(500, rv.status_code)
        self.assertEqual(b'City and Country are required params', rv.get_data())

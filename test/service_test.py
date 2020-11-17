from service.factory.api import Service, ServiceAPI
from service.factory.params import StringParameter
from unittest import TestCase
import logging


class TestServiceAPI(TestCase):
    def setUp(self):
        self.google_service = Service(
            name='Google',
            base_url='https://google.com'
        )

        self.search_api = ServiceAPI(
            name='search',
            service=self.google_service,
            method='GET',
            params=[
                StringParameter('q')
            ],
            http_headers={'content-type': 'application/json'}
        )

    def test_service_api(self):
        """
        Tests Service API Factory
        """
        rv = self.search_api.execute(q='Bogota')
        # If we recalculate the hash on the block we should get the same result as we have stored
        self.assertEqual(200, rv.status_code)

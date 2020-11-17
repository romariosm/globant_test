from service.factory.api import Service, ServiceAPI
from service.factory.params import StringParameter

__all_ = ['weather_api']


weather_service = Service(
    name='Weather Service',
    base_url='http://api.openweathermap.org/data/2.5'
)


weather_api = ServiceAPI(
    name='weather',
    service=weather_service,
    method='GET',
    params=[
        StringParameter('q'),
        StringParameter('appid'),
        StringParameter('mode')
    ],
    http_headers={'content-type': 'application/json'}
)


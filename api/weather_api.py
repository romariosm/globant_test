import json
import logging
from datetime import datetime

from flask import Blueprint, request, current_app, Response
from cache import cache

# from flasgger import swag_from
from service.weather_service import weather_api
from util.conversion import TemperatureKelvin

api = Blueprint('api', __name__)


@api.route('/weather', methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def get_weather():
    """Example endpoint returning weather dict info of a city
       ---
       parameters:
         - name: City
           in: query
           type: string
           required: true
         - name: Country
           in: query
           type: string
           required: true
       responses:
         200:
           description: Return weather city info
         500:
           description: Return error when city is not found
       """
    city = request.args.get('City')
    country = request.args.get('Country')

    if city is None and country is None:
        return Response('City and Country are required params', 500)

    result = weather_api.execute(q="{city},{country}".format(city=city, country=country),
                                 appid=current_app.config['APP_WEATHER_KEY'], mode='xml')
    if result.get('ClientError'):
        return Response(result['ClientError']['message'], 500)

    current = result['current']
    logging.warning(result)
    wind_speed = current['wind']['speed']
    city = current['city']
    temp = current['temperature']
    coord = current['city']['coord']
    response = {
        'location_name': '{},{}'.format(city['@name'], city['country']),
        'temperature': '{} °C'.format(TemperatureKelvin(float(temp['@value'])).convert_to_celsius()),
        'wind': '{}, {} {}, {}'.format(wind_speed['@name'], wind_speed['@value'], wind_speed['@unit'],
                                       current['wind'].get('@name', '')),
        'cloudiness': current['clouds']['@name'],
        'pressure': '{} {}'.format(current['pressure']['@value'], current['pressure']['@unit']),
        'humidity': '{} {}'.format(current['humidity']['@value'], current['humidity']['@unit']),
        'sunrise': datetime.strptime(current['city']['sun']['@rise'], '%Y-%m-%dT%H:%M:%S').strftime('%H:%M'),
        'geo_coordinates': [coord['@lat'], coord['@lon']],
        'requested_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return Response(json.dumps(response), content_type="application/json")


@api.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

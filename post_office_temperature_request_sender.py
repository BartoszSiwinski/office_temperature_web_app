import requests

from src.http_server.http_server import LOCALHOST_URL

post_office_temperature_url = f'http://{LOCALHOST_URL}/'

incoming_post_parms = {
    'siteId': 'abc123',
    'orgId': 'alphacorp',
    'temperature': 27.3,
    'timestamp': 1658739178
}

requests.post(post_office_temperature_url, params=incoming_post_parms)

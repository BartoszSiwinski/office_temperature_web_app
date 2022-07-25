import requests

from src.http_server.http_server import LOCALHOST_URL

post_office_temperature_url = f'{LOCALHOST_URL}post-office-temperature'

incoming_post_parms = {
    'siteId': 'abc123',
    'orgId': 'alphacorp',
    'temperature': 27.3,
    'timestamp': 1658739178
}

requests.post(LOCALHOST_URL, params=incoming_post_parms)

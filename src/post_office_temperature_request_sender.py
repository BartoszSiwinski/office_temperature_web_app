import requests

from src.http_server.http_server import url

post_office_temperature_url = f'{url}post-office-temperature'

incoming_post_parms = {
    'siteId': 'abc123',
    'orgId': 'alphacorp',
    'temperature': 27.3,
    'timestamp': 1658739178
}

requests.post(url, params=incoming_post_parms)

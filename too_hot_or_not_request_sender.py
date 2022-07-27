import requests

from src.http_server.http_server import LOCALHOST_URL

too_hot_or_not_url = f'http://{LOCALHOST_URL}/v1/admin/toohotornot/'

incoming_get_params = {
    'siteId': 'abc123'
}

requests.get(too_hot_or_not_url, params=incoming_get_params)

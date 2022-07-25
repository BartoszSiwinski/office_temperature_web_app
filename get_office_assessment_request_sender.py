import requests

from src.http_server.http_server import LOCALHOST_URL

get_office_assessment_url = f'{LOCALHOST_URL}/v1/admin/toohotornot'

incoming_get_params = {
    'siteId': 'abc123'
}

requests.get(get_office_assessment_url, params=incoming_get_params)

import requests

from main import logging


def extract(page):
    logging.info(f'Extracting for {page["name"]}')
    url = page['url']
    response = requests.get(url)

    if response.status_code == 200:
        return {'content': response.text, 'status_code': response.status_code}
    else:
        logging.error(f'Requests error on {page["name"]} has ocurred: {response.status_code}')
        return {'error': 'An error as ocurred', 'status_code': response.status_code}

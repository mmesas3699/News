import logging

import yaml

# from bs4 import BeautifulSoup

from extract import extract
from transform import transform


logging.basicConfig(
    format='%(levelname)s %(asctime)s: %(message)s',
    level=logging.INFO)


def main():
    logging.info('Begining process')

    try:
        logging.info('Reading config file...')
        config_file = open('./config.yml')
        pages = yaml.load(config_file, Loader=yaml.FullLoader)
    except Exception as e:
        logging.error(f'An error has ocurred {e}')

    for page in pages['pages']:
        extracted = extract(page)

        if 'error' in extracted:
            continue

        articles = transform(extracted, page)
        print(articles)

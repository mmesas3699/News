import os

import pymongo

from main import logging


_db = os.getenv('MONGO_INITDB_DATABASE')
_db_user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
_db_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

mongo_client = pymongo.MongoClient(f"mongodb://{_db_user}:{_db_password}@mongo:27017")
db = mongo_client[_db]
collection = db['articles']


def load(articles):
    logging.info('Saving articles...')

    try:
        collection.insert_many(articles)
    except Exception as e:
        logging.error(f'An error as ocurred: {e}')

    logging.info('Articles saved')

import re
from datetime import datetime

from bs4 import BeautifulSoup

from main import logging


def transform(extracted, page):
    logging.info(f'Cleaning data for: {page["name"]}...')

    html = BeautifulSoup(extracted['content'], 'html.parser')
    articles = html.find_all(
        page['article']['tag'],
        class_=page['article']['class'])
    data = []

    for article in articles:
        logging.info(f'Getting article from: {page["name"]}')

        _title = article.find(page['title']['tag'], class_=page['title']['class'])
        _link = article.find(page['link']['tag'], class_=page['link']['class'])
        _epigraph = article.find(page['epigraph']['tag'], class_=page['epigraph']['class'])

        title = _article_title(_title)
        link = _article_link(_link, page['url'])
        epigraph = _article_epigraph(_epigraph, _title)

        if title is None:
            continue

        _article = {
            'page': page['name'],
            'page_url': page['url'],
            'title': title,
            'link': link,
            'epigraph': epigraph,
            'date': datetime.utcnow()
        }
        data.append(_article)
    return data


def _article_title(title):
    if title is None:
        return None
    return title.text


def _article_link(link, base_url):
    if not link:
        return None

    uri = link.get('href')
    if re.match('^http.', uri):
        return uri

    return base_url + uri


def _article_epigraph(epigraph, title):
    if epigraph is None:
        return _article_title(title)
    return epigraph.text

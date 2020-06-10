import requests
import yaml

from bs4 import BeautifulSoup


def _article_title(title):
	if title is None:
		return None


def extract(page)
	url = page['url']
	response = requests.get(url)

	if response.status_code == 200:
		return response.text
	else:
		print('Ocurrio un error')


def transformed(extracted, page):
	html = BeautifulSoup(extracted)


def main(pages):
	for page in pages:
		extracted = extract(page)
		transformed = transform(extracted, page)


if __name__ == '__main__':
	config_file = open('./config.yml')
	pages = yaml.load(config_file, Loader=yaml.FullLoader)

	main(pages['pages'])

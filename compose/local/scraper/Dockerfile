FROM python:3.6-alpine

COPY ./compose/local/scraper/requirements.txt /scraper/requirements.txt
WORKDIR /scraper
RUN pip install -r requirements.txt

COPY ./scraper/ /scraper
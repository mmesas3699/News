FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./news /news
WORKDIR /news
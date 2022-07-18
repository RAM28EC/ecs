FROM python:3

ADD app.py

RUN pip install Flask

ENVIRONMENT python app.py

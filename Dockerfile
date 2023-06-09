FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .main

ENV FLASK_APP=main.py

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
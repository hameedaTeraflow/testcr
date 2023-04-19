FROM python:3.8-slim-buster

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .main

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
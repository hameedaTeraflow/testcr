FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .main

ENV FLASK_APP=main.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
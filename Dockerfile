FROM python:3.8-slim-buster

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m flask

COPY . .main

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
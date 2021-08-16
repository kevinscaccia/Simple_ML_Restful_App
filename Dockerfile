FROM python:3.8-slim-buster

RUN pip3 install flask flask-restx mysql-connector-python

WORKDIR /app
COPY . /app

CMD ["python3","app.py"]
FROM python:3.8-slim-buster

RUN pip3 install flask flask-restx mysql-connector-python

WORKDIR /app
COPY ./frontend /app

CMD ["python3","app.py"]
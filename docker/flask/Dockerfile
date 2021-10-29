FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -y install gcc default-libmysqlclient-dev

WORKDIR /app

COPY ./app /app

COPY ./docker/flask/requirements.txt /app 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "run"]
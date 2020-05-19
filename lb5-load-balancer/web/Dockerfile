FROM ubuntu:18.04

USER root

RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR /requirements
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY ./src .

EXPOSE ${URL}

ENTRYPOINT gunicorn --bind 0.0.0.0:${PORT} --workers=5 wsgi:app

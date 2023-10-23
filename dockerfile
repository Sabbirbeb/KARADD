# syntax=docker/dockerfile:1
# FROM debian:11-slim

FROM python:3.9-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app
COPY ./static /code/static
COPY ./scripts /code/scripts
COPY ./templates /code/templates
COPY ./assets /code/assets

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]

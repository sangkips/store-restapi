FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt update && apt install --no-install-recommends -y \
  build-essential \
  libpq-dev

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

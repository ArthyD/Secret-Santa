FROM python:3.8-alpine
WORKDIR /website
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /website
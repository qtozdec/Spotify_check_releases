FROM python:3.8

RUN mkdir /src
WORKDIR /src
copy . /src
RUN pip install -r requirements.txt

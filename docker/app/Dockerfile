FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY ./backend .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

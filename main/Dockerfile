FROM python:3.12
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=manager.py
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app


FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY /src/ /app/src

ENV FLASK_APP=/app/src/main.py
ENV PORT=5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --chdir src/ main:app
from python:3.9-slim

workdir /app

copy . /app



cmd ["python", "app.py"]


FROM python:3.12-bullseye

WORKDIR /usr/src/Ravys_Project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD gunicorn Ravys_Project.wsgi:application -b 0.0.0.0:8000
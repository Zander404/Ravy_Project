FROM python:3.8.13-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/app

COPY requirements.txt .
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/app . 

EXPOSE 8000
CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT


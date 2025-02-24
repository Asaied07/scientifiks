FROM python:alpine

WORKDIR /scientifiks

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    python3-dev

COPY ./scientifiks .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
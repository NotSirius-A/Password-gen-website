FROM python:3.9.5-slim

COPY requirements.txt /requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

# WORKDIR /app

ADD . .

EXPOSE 8000

COPY ./entry_point.sh /
ENTRYPOINT ["sh", "/entry_point.sh"]


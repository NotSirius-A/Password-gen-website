FROM python:3.9.5-slim

WORKDIR /my_app

COPY ./word_list/word_list_prod.csv ./word_list/word_list_prod.csv

COPY ./deployment/django/requirements.txt .

COPY ./src/ ./src/

EXPOSE 8000

COPY ./deployment/django/entry_point.sh .
ENTRYPOINT ["sh", "entry_point.sh"]


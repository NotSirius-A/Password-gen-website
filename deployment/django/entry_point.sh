#!/bin/sh

pwd
ls

set -ex && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

cd src

python manage.py collectstatic --no-input

gunicorn my_core.wsgi -b 0.0.0.0:8000


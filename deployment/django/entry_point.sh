#!/bin/sh

cd src
python manage.py collectstatic --no-input

gunicorn school_website.wsgi -b 0.0.0.0:8000


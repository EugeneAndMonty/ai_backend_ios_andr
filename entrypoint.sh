#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn ai_backend_ios_andr.wsgi:application --bind 0.0.0.0:80 --workers 3 -k "gevent"
gunicorn --limit-request-line 0
#!/bin/sh

cd src
python manage.py migrate --fake-initial --no-input
python manage.py collectstatic --no-input

gunicorn service_sales_app.wsgi:application --bind 0.0.0.0:8000

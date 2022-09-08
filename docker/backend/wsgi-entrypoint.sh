#!/bin/sh

until cd /app/backend/
do
    echo "Waiting for server volume..."
done

until ./manage.py makemigrations && ./manage.py migrate && ./manage.py load

do
    echo "Waiting for db to be ready..."
    sleep 2
done

./manage.py collectstatic --noinput

./manage.py runserver 0.0.0.0:5000

#!/bin/bash

service redis-server start

echo "Collect static files" 
#python manage.py collectstatic --noinput


echo "Apply database migrations"
python manage.py migrate

echo "Populating database"
exec python manage.py populate_db

echo "Populating views"
exec python manage.py populate_views

echo Starting server..
exec python manage.py thrift_server

#!/bin/bash
python3 manage.py collectstatic --noinput &&
python3 manage.py makemigrations &&
python3 manage.py collectstatic &&
python3 manage.py migrate &&
uwsgi --ini /root/xiaoe_testing_platform/docker/xiaoe_testing_platform/uwsgi.ini
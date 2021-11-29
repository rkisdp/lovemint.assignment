#!/bin/sh
set -e
python manage.py collectstatic --noinput
echo "===Running Migrate==="
python manage.py migrate --noinput
echo "===END==="
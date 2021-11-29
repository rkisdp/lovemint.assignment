#!/bin/bash
set -e
echo "===Initiating Celery==="
celery -A lovemint_django_backend.celery worker -l info

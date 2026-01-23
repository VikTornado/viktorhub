#!/bin/sh

# Wait for database if needed (optional but recommended for production)
# echo "Waiting for database..."
# sleep 5

echo "Applying database migrations..."
python manage.py migrate --noinput

# Optional: Run seed data if it's the first time
# echo "Seeding initial data..."
# python manage.py seed_data

echo "Starting server..."
exec gunicorn --bind 0.0.0.0:8000 vikhub.wsgi:application

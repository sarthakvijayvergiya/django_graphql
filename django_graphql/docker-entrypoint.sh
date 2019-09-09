#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py migrate auth

# Create superuser
echo "Creating superuser"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'sarthakvijayvergiya@gmail.com', 'admin')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

# if the server exits, sleep so we can do other things
sleep 6000
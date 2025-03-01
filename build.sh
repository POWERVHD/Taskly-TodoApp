#!/bin/bash

echo "Starting build script..."

# Exit script on any error
set -e  

# Activate virtual environment (uncomment if needed)
# source venv/bin/activate  

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Applying migrations..."
python clear_sessions.py  # Run this before migrations to clear sessions
python manage.py makemigrations
python manage.py migrate

#echo "Collecting static files..."
#python manage.py collectstatic --noinput


echo "Build completed successfully!"

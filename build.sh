#!/bin/bash

echo "Starting build script..."

# Exit script on any error
set -e  

# Activate virtual environment (uncomment if needed)
# source venv/bin/activate  

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate


echo "Build completed successfully!"

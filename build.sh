#!/usr/bin/env bash
# Stop execution if any command fails
set -e

echo " Starting build script for Django project....."

# Upgrade pip
echo " Upgrading pip...."
pip  insatll --upgrade pip

# Install dependencies
echo " Installing dependencies from requirements.txt....."
pip install -r requirements.txt

# Apply db migrations
echo " Running Django migrations...."
python manage.py migrate --noinput

# Collect static files.....
python manage.py collectstatic --noinput

echo " Build script finished successfully!"
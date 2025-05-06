#!/bin/bash

# entrypoint.sh

# Exit on error
set -e

# Run database migrations
python manage.py migrate

# Collect static files (optional)
# python manage.py collectstatic --noinput

# Start server
exec "$@"

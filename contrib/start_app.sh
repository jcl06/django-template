#!/bin/sh
/app/venv/bin/gunicorn --pid /var/tmp/app.pid --pythonpath /app --config /app/gunicorn.py configs.wsgi
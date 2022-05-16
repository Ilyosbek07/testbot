#!/bin/bash
source /home/www/code/testolog/env/bin/activate
exec gunicorn -c "/home/www/code/testolog/backend/gunicorn_config.py" backend.panel.panel.wsgi

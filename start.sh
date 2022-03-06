#!/bin/bash
cd extras
source venv/bin/activate
uwsgi --ini web_app.ini &
uwsgi --ini web_cache.ini

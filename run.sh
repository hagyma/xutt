#!/bin/bash

source /home/globalarts/.pythonbrew/etc/bashrc

cd /home/globalarts/xutt

pythonbrew switch $2
pythonbrew venv use $3
exec python manage.py run_gunicorn -w 3 -b 127.0.0.1:$1 --log-level=debug -k gevent 


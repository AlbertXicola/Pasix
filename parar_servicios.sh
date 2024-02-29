#!/bin/bash

kill $(pgrep -f "python3 Django/manage.py runserver")

sleep 5

kill $(pgrep -f "sudo python3 Django/Django_Flask/progrm/pycore.py")

sleep 5

sudo docker-compose down

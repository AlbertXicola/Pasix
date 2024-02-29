#!/bin/bash

gnome-terminal -- python3 Django/manage.py runserver &

sleep 5

gnome-terminal -- sudo python3 Django/Django_Flask/progrm/pycore.py &

sleep 5

gnome-terminal -- sudo docker-compose up &

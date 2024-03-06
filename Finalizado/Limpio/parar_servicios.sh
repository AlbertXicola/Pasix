#!/bin/bash

echo -n "Introduce tu contraseña: "
read -s password
echo

pkill -f "python3 Django/manage.py runserver"
pkill -f "python3 Django/Django_Flask/progrm/pycore.py"

deactivate 2>/dev/null

echo "$password" | sudo -S docker-compose down

echo "$password" | sudo -S rm -rf venv

echo "Servicios apagados exitosamente."

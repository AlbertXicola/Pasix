#!/bin/bash

echo -n "Introduce tu contraseña: "
read -s password
echo

python3 manage.py runserver &

chmod +x venv/bin/activate
source venv/bin/activate

pip3 install pymongo
pip3 install pillow
pip3 install django-admin-interface
pip3 install flask
pip3 install django
pip install requests pymongo Flask

python3 Django/manage.py runserver &
sleep 5
python3 Django/Django_Flask/progrm/pycore.py &
sleep 5
echo "$password" | sudo -S docker-compose up &

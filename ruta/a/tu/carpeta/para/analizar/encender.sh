cd Descargas/
cd Pasix/
cd Downloads/
cd Pasix/



virtualenv venv
chmod +x venv/bin/activate
source venv/bin/activate

pip3 install pymongo
pip3 install pillow
pip3 install django-admin-interface 
pip3 install flask 
pip3 install django
pip install requests pymongo Flask

python manage.py makemigrations
python manage.py migrate
gnome-terminal -- python3 Django/manage.py runserver 


sleep 5
python manage.py makemigrations
python manage.py migrate

gnome-terminal -- python3 Django/Django_Flask/progrm/pycore.py runserver 

sleep 5

gnome-terminal -- sudo docker-compose up 

cd Descargas/
cd Pasix/
cd Downloads/
cd Pasix/


code .


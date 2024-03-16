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
pip3 install django
pip3 install djongo
pip3 install requests
pip install django-avatar



cd Django/

python manage.py makemigrations 
python manage.py migrate app zero
python manage.py migrate


cd ..

gnome-terminal -- python3 Django/manage.py runserver 

sleep 5

gnome-terminal -- sudo docker-compose up 

cd Descargas/
cd Pasix/
cd Downloads/
cd Pasix/


code .


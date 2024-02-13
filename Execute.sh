sudo apt update
echo 's' | sudo apt install python3 python3-pip -y

sudo apt install python3.11-venv

echo 's' | sudo apt install python3-pip

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
pip3 install pymongo
pip3 install pillow
pip3 install django-admin-interface 
pip3 install flask 
pip3 install django

wget https://downloads.mongodb.com/compass/mongodb-compass_1.42.0_amd64.deb
sudo apt install ./mongodb-compass_1.42.0_amd64.deb
sudo chmod +r /home/pasix/mongodb-compass_1.42.0_amd64.deb
sudo apt install ./mongodb-compass_1.42.0_amd64.deb

echo 's' | sudo apt install curl

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

echo 's' | sudo apt install docker.io
sudo docker ps
sudo apt install git

git clone https://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@github.com/AlbertXicola/Pasix

cd Pasix

sudo apt install expect

gnome-terminal -- python3 Django/manage.py runserver

sleep 5

gnome-terminal -- python3 Django/Django_Flask/progrm/pycore.py runserver

sleep 5

gnome-terminal -- sudo docker-compose up


sleep 60

MONGODB_IP=$(sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docker-compose)

# Construir la cadena de conexión con la IP obtenida
CONEXION="mongodb://pasix:20Logicalis21@$MONGODB_IP:27017/Proyecto"

# Usar la variable CONEXION en lugar de la dirección IP estática
mongodb-compass $CONEXION
xdg-open http://localhost:8000


exit

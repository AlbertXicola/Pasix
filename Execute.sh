sudo apt update
sudo apt install python3 python3-pip -y

sudo apt install python3.11-venv


sudo apt install python3-pip
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


sudo apt install curl

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose


sudo apt install docker.io
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


sleep 20

mongodb-compass mongodb://pasix:20Logicalis21@1172.19.16.1:27017/Proyecto

xdg-open http://localhost:8000
exit

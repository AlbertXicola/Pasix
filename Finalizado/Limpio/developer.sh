sudo apt update

sudo apt install python3.11-venv -y

sudo apt install python3 python3-pip -y

pip install virtualenv

sudo apt install python3-virtualenv -y

virtualenv venv

chmod +x venv/bin/activate

source venv/bin/activate



pip install requests pymongo Flask

sudo apt install python3 python3-pip -y
sudo apt install python3.11-venv -y

sudo apt install python3-pip -y

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED -y
pip3 install pymongo
pip3 install pillow
pip3 install django-admin-interface 
pip3 install flask 
pip3 install django


wget https://downloads.mongodb.com/compass/mongodb-compass_1.42.0_amd64.deb

sudo apt install ./mongodb-compass_1.42.0_amd64.deb
sudo chmod +r /home/pasix/mongodb-compass_1.42.0_amd64.deb
sudo apt install ./mongodb-compass_1.42.0_amd64.deb

sudo apt install curl -y

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose


sudo apt install docker.io -y
sudo docker ps -y
sudo apt install git -y

git clone https://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@github.com/AlbertXicola/Pasix

cd Pasix

sudo apt install expect -y

sudo apt install software-properties-common apt-transport-https wget -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo mv packages.microsoft.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install code -y

gnome-terminal -- python3 Django/manage.py runserver 

sleep 5

gnome-terminal -- python3 Django/Django_Flask/progrm/pycore.py runserver 

sleep 5

gnome-terminal -- sudo docker-compose up 

echo "============================================================================"
echo "En 50 segundos o más, se va abrir el visual estudio y el docker."
echo "No acceptar la Extension de python en el Visual Studio Code, ir tu al apaartado e darle a install"
echo "Pulse en la consola de la pagina localhost, si no se abre el buscador, abralo manualmente (http://localhost:8000)"
echo "Finalizado, NO CIERRE NI TOQUE ESTA VENTANTA, NI NINGUNA EJECUTADA POR EL PROGRAMA"
echo "============================================================================"


sleep 40

code .
mongodb-compass mongodb://pasix:20Logicalis21@localhost:27017/
xdg-open http://localhost:8000
firefox http://localhost:8000

exit

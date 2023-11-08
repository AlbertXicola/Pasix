#!/bin/bash

# Actualizar la lista de paquetes e instalar las herramientas necesarias
sudo apt update
sudo apt install -y curl

# Instalar MongoDB
echo "Instalando MongoDB..."
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
echo "MongoDB instalado y en ejecución."

# Instalar MariaDB
echo "Instalando MariaDB..."
sudo apt install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
echo "MariaDB instalado y en ejecución."

# Instalar Django (y sus dependencias)
echo "Instalando Django y sus dependencias..."
sudo apt install -y python3-pip python3-venv
pip3 install Django
echo "Django instalado."

echo "Instalación completa: MongoDB, MariaDB y Django están listos para su uso."

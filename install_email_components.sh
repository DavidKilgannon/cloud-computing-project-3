cd /local/repository/mailu

# Apache

apt-get update
apt-get -y install apache2

# MySQL and PHP

apt-get update
apt-get -y install mysql-server
apt-get -y install php

# Mailu

sudo current_ip=$(wget -qO- http://ipecho.net/plain ; echo)
sudo sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' docker-compose.yml
sudo sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' mailu.env
sudo docker-compose -p mailu up -d
sudo docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

# This should write to the user's console even from inside the shell script.

echo "Mail Server is Ready!" | tee welcome.txt
echo "$current_ip" | tee welcome.txt

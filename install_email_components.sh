cd /local/repository/

# Apache

apt-get update
apt-get -y install apache2

# MySQL and PHP

apt-get update
apt-get -y install mysql-server
apt-get -y install php

cd mailu
# Mailu
current_ip=$(hostname -i)
sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' docker-compose.yml
sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' mailu.env


# This should write to the user's console even from inside the shell script.

echo "Mail Server is Ready!" | tee welcome.txt
echo "$current_ip" | tee welcome.txt

cd ..
sudo docker-compose up

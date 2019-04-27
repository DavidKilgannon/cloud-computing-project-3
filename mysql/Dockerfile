FROM ubuntu: 18.04

RUN 	apt-get -y install mysql-server
	apt -y install phpmyadmin php-mbstring php-gettext
	service apache2 restart 
	service mysql-server restart

EXPOSE 80

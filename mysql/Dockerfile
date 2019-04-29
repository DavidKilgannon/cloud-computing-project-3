FROM ubuntu:16.04
RUN apt-get -y install mysql-server
RUN apt -y install phpmyadmin php-mbstring php-gettext
RUN service apache2 restart 
RUN service mysql-server restart
EXPOSE 80

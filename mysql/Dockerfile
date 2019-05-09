FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install mysql-server
RUN sudo apt-get install php7.0 php7.0-fpm php7.0-mysql -y
RUN service apache2 restart 
RUN service mysql-server restart
EXPOSE 81

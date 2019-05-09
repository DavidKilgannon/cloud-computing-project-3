FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install mysql-server
RUN sudo apt-get install php7.2 -y
RUN sudo apt-get install php7.2-fpm -y
RUN sudo apt-get install php7.2-mysql -y
RUN service apache2 restart 
RUN service mysql-server restart
EXPOSE 81

FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install postfix
RUN //scrolls down
RUN 2 //chooses Internet site
RUN	Group 9 Mail Server //naming
RUN service postfix restart 
RUN apt-get -y install dovecot-imapd dovecot-pop3d // -y flag here may put into infinite loop. test.
RUN service dovecot restart 

///////

RUN apt-get update
RUN apt-get wget
RUN cd var
RUN mkdir www
RUN cd www
RUN wget http://sourceforge.net/projects/squirrelmail/files/stable/1.4.21/squirrelmail-1.4.21.tar.gz
RUN tar -zxvf squirrelmail-1.4.21.tar.gz
RUN mv squirrelmail-1.4.21 webmail
RUN cd webmail
RUN ./configure

//organization name
RUN 1
RUN 1
RUN Group 9
RUN R

RUN	2
RUN	1
RUN	group9.com
RUN	R
RUN 4
RUN	11
RUN y
//save and quit
RUN S
RUN
RUN Q

RUN cd.. [for go to previous directory… now we will be at /var/www/ directory…]
RUN chown -R www-data:www-data webmail/
RUN cd /var/www/webmail/
RUN chown -R www-data:www-data data/
//attachments - Max 2 MB
RUN mkdir attach
RUN chown -R www-data:www-data attach/

RUN cp /var/www/webmail/config/config.php /etc/apache2/sites-available/squirrelmail.conf 
RUN a2ensite squirrelmail.conf 
RUN	useradd student 
RUN	passwd goldenram 
RUN mkdir -p /var/www/html/student 
RUN usermod -m -d /var/www/html/student student 
RUN chown -R student:student /var/www/html/student
EXPOSE 80

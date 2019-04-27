FROM ubuntu:18.04
RUN	apt-get update
RUN apt-get -y install postfix \
	Internet Site\n \
	Group 9 Mail Server\n 
RUN service postfix restart 
RUN apt-get install dovecot-imapd dovecot-pop3d 
RUN service dovecot restart 
RUN apt-get install squirrelmail 
RUN squirrelmail-configure \
	2\n \
	1\n \
	group9.com\n \
	R\n4\n \
	11\ny\n 
RUN cp /etc/squirrelmail/apache.conf /etc/apache2/sites-available/squirrelmail.conf 
RUN a2ensite squirrelmail.conf \
	useradd student \
	passwd goldenram 
RUN mkdir -p /var/www/html/student 
RUN usermod -m -d /var/www/html/student student 
RUN chown -R student:student /var/www/html/student
EXPOSE 80

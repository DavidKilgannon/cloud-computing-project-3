FROM ubuntu:18.04
RUN apt-get -y install postfix
RUN	Internet Site\n 
RUN	Group 9 Mail Server\n 
RUN service postfix restart 
RUN apt-get install dovecot-imapd dovecot-pop3d 
RUN service dovecot restart 
RUN apt-get install squirrelmail 
RUN squirrelmail-configure 
RUN	2\n
RUN	1\n
RUN	group9.com\n
RUN	R\n4\n
RUN	11\ny\n 
RUN cp /etc/squirrelmail/apache.conf /etc/apache2/sites-available/squirrelmail.conf 
RUN a2ensite squirrelmail.conf 
RUN	useradd student 
RUN	passwd goldenram 
RUN mkdir -p /var/www/html/student 
RUN usermod -m -d /var/www/html/student student 
RUN chown -R student:student /var/www/html/student
EXPOSE 80

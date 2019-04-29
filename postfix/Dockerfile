FROM ubuntu:18.04
RUN apt-get update
# should find it now...
RUN apt-get -y install postfix
# blank run scrolls down configure page...
RUN  
RUN 2
RUN	Group 9 Mail Server
RUN service postfix restart 
# the dovecot y flag put me into an infinite loop...
RUN apt-get install dovecot-imapd dovecot-pop3d
RUN Y
RUN service dovecot restart 

# new stuff - SquirrelMail is not supported in ubuntu 18.04 as a package...

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

# organization name
RUN 1
RUN 1
RUN Group 9
RUN R
# domain name
RUN	2
RUN	1
RUN	group9.com
RUN	R
# turn on server-side sort option
RUN 4
RUN	11
RUN y
# save and quit
RUN S
RUN
RUN Q

RUN cd ..
RUN chown -R www-data:www-data webmail/
RUN cd /var/www/webmail/
RUN chown -R www-data:www-data data/
# attachments data - Max 2 MB attachments
RUN mkdir attach
RUN chown -R www-data:www-data attach/

# Stops working at line 55 - 56

RUN cp /var/www/webmail/config/config.php /etc/apache2/sites-available/squirrelmail.conf 
RUN a2ensite squirrelmail.conf 
RUN	useradd student 
RUN	passwd goldenram 
RUN mkdir -p /var/www/html/student 
RUN usermod -m -d /var/www/html/student student 
RUN chown -R student:student /var/www/html/student
EXPOSE 82

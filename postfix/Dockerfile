FROM ubuntu:18.04
RUN cd /local/repository/postfix
RUN docker-compose -p mailu up -d
RUN docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

EXPOSE 82

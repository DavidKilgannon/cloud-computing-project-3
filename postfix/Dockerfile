FROM ubuntu:18.04
RUN cd /local/
RUN cd ..
RUN mkdir /mailu
RUN cd /mailu
RUN wget http://setup.mailu.io/1.6/file/a9f58d42-0a83-4200-b62c-f58bd0680df1/docker-compose.yml
RUN wget http://setup.mailu.io/1.6/file/a9f58d42-0a83-4200-b62c-f58bd0680df1/mailu.env
RUN docker-compose -p mailu up -d
RUN docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

EXPOSE 82

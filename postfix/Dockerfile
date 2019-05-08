FROM ubuntu:18.04
RUN cd /local/repository/postfix
RUN current_ip=$(wget -qO- http://ipecho.net/plain ; echo)
RUN sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' docker-compose.yml
RUN sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' mailu.env
RUN docker-compose -p mailu up -d
RUN docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

# NOTE: You can open mailu in the shell with 
# apt install xdg-utils
# xdg-open http://127.0.0.1:8080/ui 

EXPOSE 82

FROM ubuntu:18.04
RUN cd mailu
RUN sudo current_ip=$(wget -qO- http://ipecho.net/plain ; echo)
RUN sudo sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' docker-compose.yml
RUN sudo sed -i -e 's/OVERWRITETHIS/'$current_ip'/g' mailu.env
RUN sudo docker-compose -p mailu up -d
RUN sudo docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

# NOTE: it works on a web browser!
# http://[YOUR CLOUD COMPUTERS IP]/

# NOTE: You can open mailu in the shell with 
# apt install xdg-utils
# xdg-open http://[YOUR IP]/

# The IP address is found in nano docker-compose.yml - scroll to the list of ports. this is your cloud computer's IP address.
# username: admin@group9.com
# password: group9rules

EXPOSE 82

FROM ubuntu:18.04
WORKDIR mailu
RUN apt-get update
RUN docker-compose -p mailu up -d
RUN docker-compose -p mailu exec admin flask mailu admin admin group9.com group9rules

# NOTE: it works on a web browser!
# http://[YOUR CLOUD COMPUTERS IP]/

# NOTE: You can open mailu in the shell with 
# apt install xdg-utils
# xdg-open http://[YOUR IP]/

# The IP address is found in nano docker-compose.yml - scroll to the list of ports. this is your cloud computer's IP address.
# username: admin@group9.com
# password: group9rules

EXPOSE 82

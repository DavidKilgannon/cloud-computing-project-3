import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Description of System
tourDescription = \
"""
This is our profile for the cloud computing project.
Our anticipated features are an Apache webserver
A MySQL database (or something similar)
A Postfix mail server
"""
#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

#code from cluster-template, if we want to use CENTOS7 instead AND have additional nodes.
#prefixForIP = "192.168.1."
#link = request.LAN("lan")
#for i in range(6):
# if i == 0:
#   node = request.XenVM("head")
#   node.routable_control_ip = "true"
# elif i == 1:
#   node = request.XenVM("metadata")
# elif i == 2:
#   node = request.XenVM("storage")
# else:
#   node = request.XenVM("compute-" + str(i-2))
#   node.cores = 4
#   node.ram = 4096
    
# node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
  
# iface = node.addInterface("if" + str(i))
#  iface.component_id = "eth1"
#  iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
#link.addInterface(iface)
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

node.addService(rspec.Execute(shell="/bin/sh",
                              command="sudo bash /local/repository/setup.sh"))
#node.addService(rspec.Execute(shell ="sh",
#                             command = "sudo /local/repository/setup.sh")

#node.addService(rspec.Execute(shell="/bin/sh",
#                              command="sudo apt update"))
#node.addService(rspec.Execute(shell="/bin/sh",
#                              command="sudo apt install -y apache2"))
#node.addService(rspec.Execute(shell="/bin/sh",
#                              command='sudo ufw allow in "Apache Full"'))
#node.addService(rspec.Execute(shell="/bin/sh",
#                              #command='sudo systemctl status apache2'))
# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

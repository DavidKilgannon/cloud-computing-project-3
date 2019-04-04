# cloud-computing-project-3
Team Members: David Kilgannon, Daniel Jankowski, Tyler Heller, Cameron Brown

(Consult history to see dates changed)

Project Option 3

	To Do:
		Install and deploy a multi-node computing service on CloudLab's OpenStack Cloud.
			Select a computing service consisting of at least two service nodes (i.e., a web server
			with a backend SQL server OR a Big Data Analytics Hadoop cluster with namenode and datanodes)
			and deploy the corresponding VMs inside CloudLab's OpenStack infrastructure.
			
			
		Subtasks
			Able to setup VM nodes (possibly on local computers) that work together to provide a unified
			computing service to users.
			
			Able to move these VM nodes into the Cloud, setup proper network environment, and link them together.
	
	Deliverables
		1
			Team Description (This)
			Documentation describing the selected computing service, including network diagram and specific
			details on what services being installed on which VM.
			
			Implementation:
			
			We have chosen to install an Apache webserver on an Ubuntu machine using a simple apache2 installation.
			
			We will be adding a MySQL database to serve as a backend to the webserver. 
			
			We will be installing a Postfix mail server. An excellent resource for this installation has been cited
			in our Resources document.
			
			An Apache solution called Cloudstack is currently under consideration for implementation.
			It is a cloud-based service that is easily scalable. See the resource provided in Resources.
			
			Testing:
			
			Our previous experience in testing Apache and MySQL has been within Cloudlab. As a result, the testing
			process has been time-consuming.
			
			At the recommendation of our professor, we will test in Docker via a Microsoft Professional
			Operating System. A free version of Microsoft Professional has been provided to us as university students.
			
			The setup of Docker should be simple. A resource has been given in Resources.
			
		2
			In-class demonstration of the selected computing services on local machines or on CloudLab
			(may or may not be automated on CloudLab)
			
			If readily possible it will be automated by this point.
		3
			Project report and/or GitHub repository contains the fully automated profile.

## Installing Local Mongodb (community addition)

1. [Installation Steps](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

1. Import the public key used by the package management system

	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
	
1. Create a list file for MongoDB (Ubuntu 16.04)
	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
	
1. Reload local package database.
	sudo apt-get update
	
1. Install the MongoDB packages
	sudo apt-get install -y mongodb-org
	
1. Start Mongodb 
	sudo service mongodb start
	
2. Stop Mongodb
	sudo service mongodb stop
	
3.Start using mongodb with mongo shell
	mongo --host 127.0.0.1:27017
	
  ctrl+C to quit mongo shell
	
**Uninstall Mongodb in Ubuntu linux**
1.	Stop MongoDB service if service is online
	sudo service mongod stop
2. Remove Packages.
	sudo apt-get purge mongodb-org*
3. Remove Data Dierctories
	sudo rm -r /var/log/mongodb
	sudo rm -r /var/lib/mongodb
	
**Next [Set up the Python Environment](02-Environment.md)

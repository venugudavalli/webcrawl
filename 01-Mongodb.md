## Installing Local Mongodb (community addition)

1. Installation Steps [for latest updates](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

1. Import the public key used by the package management system

	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
	
1. Create a list file for MongoDB (Ubuntu 16.04)

	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
	
1. Reload local package database.
	
	sudo apt-get update
	
1. Install the MongoDB packages
	
	sudo apt-get install -y mongodb-org
	
1. Check the mongodb installation version

		$ mongod --version	
		db version v4.0.0
		git version: 3b07af3d4f471ae89e8186d33bbb1d5259597d51
		OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
		allocator: tcmalloc
		modules: none
		build environment:
	    		distmod: ubuntu1604
	    	distarch: x86_64
	    	target_arch: x86_64
	
1. Start Mongodb 
	
	sudo service mongodb start
	
		If you are using Ubuntu 16.04, you may run into an issue where you see the error mongodb: unrecognized service due to the switch from upstart to systemd. To get around this, you have to follow these steps. [follow the link here](https://www.techrepublic.com/article/how-to-install-mongodb-community-edition-on-ubuntu-linux/)

		If you added the /etc/apt/sources.list.d/mongodb-org.list, remove it with the command sudo rm /etc/apt/sources.list.d/mongodb-org.list.
		Update apt with the command sudo apt-get update.
		Install the official MongoDB version from the standard repositories with the command sudo apt-get install mongodb in order to get the service set up properly.
		Remove what you just installed with the command sudo apt-get remove mongodb && sudo apt-get autoremove.
		Follow the instructions I outlined earlier for installing MongoDB; this should re-install the latest version of MongoDB with the systemd services already in place. When you issue the command systemctl status mongodb you should see that the server is active 
	
2. Stop Mongodb
	
	sudo service mongodb stop
	
3. Start using mongodb with mongo shell
	
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

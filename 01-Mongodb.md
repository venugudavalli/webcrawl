**Main**:[Home](Readme.md)|| **Next**: [Setup the environment](02-Setup_Environment.md)
## 1. Installing Local Mongodb (community addition)

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
	
	**If you are using Ubuntu 16.04, you may run into an issue where you see the error**
<font color="red">error mongodb: unrecognized service</font> due to the switch from upstart to systemd. To get around this, you have to follow these steps.** [follow the link here](https://www.techrepublic.com/article/how-to-install-mongodb-community-edition-on-ubuntu-linux/)
	
or 
[go to workaround](mongodb-install-workaround.md)
 
	
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
	
**Main**:[Home](Readme.md)|| **Next:** [Setup the Environment](02-Setup_Environment.md)

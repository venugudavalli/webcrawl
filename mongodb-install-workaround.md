**Steps to Install mongodb on Ubuntu for free** 

[article on techrepublic.com](https://www.techrepublic.com/article/how-to-install-mongodb-community-edition-on-ubuntu-linux/)

  There are different versions of MongoDB; but let us focus on the community edition. 
  
  You can easily install MongoDB on Ubuntu from the standard repositories, but that version tends to be out of date. Because of that, we will install the version from the official MongoDB repositories. 
	
1. This repository will install:

  	- mongodb-org (this is the meta package that will install everything below)
  	- mongodb-org-server (the mongod daemon)
 	- mongodb-org-mongos (the mongos daemon)
  	- mongodb-org-shell (the mongo shell)
  	- mongodb-org-tools (the MongoDB tools package which includes import, dump, export, files, performance, restore, and stats tools)

The package we will install only provides support for 64-bit architecture. This package also only officially supports Long Term Support (LTS) releases (12.04, 14.04, 16.04); other releases may work, but not as a supported configuration (there is an installation issue with Ubuntu 16.04 that I will address later).

The first step is add the MongoDB repository. To do this, you must import the MongoDB public key. Here's how.
Open a terminal window.

1. Issue the command 
	- sudo apt-key adv —keyserver hkp://keyserver.ubuntu.com:80 —recv EA312927.
			
2. Issue the command

	- sudo touch /etc/apt/sources.list.d/mongodb-org.list.
			
3. Issue the command 

	- sudo nano /etc/apt-sources.list.d/mongodb-org.list.
	
Copy and paste one of the following lines from below (depending upon your release) into the open file.
		
	For 16.04*: 
	- deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse
		
	- Hit [Ctrl]+[x] to save the file.

** Note: Getting MongoDB community edition running successfully on Ubuntu 16.04 is challenging. 

Find the workaround after the standard installation steps below.

**Installing MongoDB

1. Open a terminal window.
2. Update apt with the command 
	- sudo apt-get update.
3. Once apt has updated, install MongoDB with the command 
	- sudo apt-get install -y mongodb-org.
4. Allow the installation to complete.
5. Running the community edition

**To start the database, issue the command sudo service mongodb start. You should now be able to issue the command to see that MongoDB is running: systemctl status mongodb.**

**Ubuntu 16.04 solution**
		
1. If you are using Ubuntu 16.04, you may run into an issue where you see the error mongodb: unrecognized service due to the switch from upstart to systemd. To get around this, you have to follow these steps.

1. If you added the /etc/apt/sources.list.d/mongodb-org.list, remove it with the command 

	sudo rm /etc/apt/sources.list.d/mongodb-org.list.
			
2. Update apt with the command 

	sudo apt-get update.

3. Install the official MongoDB version from the standard repositories with the command 

	sudo apt-get install mongodb in order to get the service set up properly.

4. Remove what you just installed with the command 
		
	sudo apt-get remove mongodb && sudo apt-get autoremove
		
5. Follow the instructions outlined earlier for installing MongoDB; this should re-install the latest version of MongoDB with the systemd services already in place. When you issue the command systemctl status mongodb you should see that the server is active

The MongoDB server is now running on Ubuntu 16.04.

**Time to play**

You now have a working instance of MongoDB, and you can start learning the ins and outs of a database used by big data and enterprise companies—a good place to start is the official MongoDB manual. If you're looking for a forum with answers to your questions, check out this MongoDB Google Group.

Also see
- [Why some of the fastest growing databases are also the most experimental](https://www.techrepublic.com/article/why-some-of-the-fastest-growing-databases-are-also-the-most-experimental/) (TechRepublic)

- [MongoDB and Cassandra put relational databases on notice](https://www.techrepublic.com/article/mongodb-and-cassandra-put-relational-databases-on-notice/) (TechRepublic)

- [Big data startups beware: Disruption isn't enough, you need to make money](https://www.techrepublic.com/article/big-data-startups-beware-disruption-isnt-enough-you-need-to-make-money/) (TechRepublic)

- [Microsoft cozies up to Ubuntu as developers welcome cold day in hell](http://www.zdnet.com/article/microsoft-cozies-up-to-ubuntu-as-developers-welcome-cold-day-in-hell/) (ZDNet)

- [Job description: Big data modeler](http://www.techproresearch.com/downloads/job-description-big-data-modeler/) (Tech Pro Research)



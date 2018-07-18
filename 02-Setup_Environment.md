**Previous** [Install Mongodb](01-Mongodb.md) || **Next** [Setup Scraper](03-setup_scraper.md) 						
## 2. Setup Python Environment

### Setting up folder Structure
0 level or root folder ted-scraper
	- level 1 tedbot
		- level 2 spiders
copy or cerate below files into ted-scraper folder
	- environment.yml
	- scrapy.cfg
	
### Creating new python virtual environment tedbot

**file: environment.yml**

add below lines to the environment.yml file with required packages

name: tedbot
channels:
  - conda-forge
dependencies:
  - python=3.6
  - beautifulsoup4
  - scrapy
  - pip:
    - pymongo
		
1. open terminal and navigate to ted-scraper root folder and execute below command
	
	conda env create -f environment.yml
	
2. Activate virtual environment

	source activate tedbot
	
3. Check active environment

	conda env list 
	
	Active environment is prefixed with * in the list
	

**Next**: [Setup Scraper](03-setup_scraper.md)

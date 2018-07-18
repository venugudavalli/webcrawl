**Previous**: [Setup the environment](02-Setup_Environment.md) || **Next**: [Run Scraper](04-Run_Scraper.md)
## 3. Setup Scraper
### configuration file : scrapy.cfg
This will provide default scraper bot settings for scraper. 
Provides Project name for deployment.
**tedbot/pipelines.py**
pipelines.py file 
this file will define data pipeline classes and methods
  1. Required to handle request/response/and parsing web data
  2. Required to connect and write data into mongodb 
  
**tedbot/settings.py

This file provides settings for the project level that allows you to customize the behaviour of all Scrapy components, 
  - including the core, 
  - extensions, 
  - pipelines and 
  - spiders themselves.
  
### BOT_NAME = '<name of bot>' must be unique the project

### SPIDER_MODULES
A list of modules where Scrapy will look for spiders.
SPIDER_MODULES = ['tedbot.spiders'] 

AUTOTHROTTLE_ENABLED = True

### ITEM_PIPELINES
Default: {}

A dict containing the item pipelines to use, and their orders. Order values are arbitrary, but it is customary to define them 
in the 0-1000 range. Lower orders process before higher orders.

ITEM_PIPELINES = {

    'tedbot.pipelines.TimingsDownloaderPipeline': 100,
    'tedbot.pipelines.TranscriptDownloaderPipeline': 100,
    'tedbot.pipelines.MongoPipeline': 200,
}

### Database connection settings
MONGO_URI = 'mongodb://localhost:27017'

MONGO_DATABASE = 'ted'

**Previous**: [Setup the environment](02-Setup_Environment.md) || **Next**: [Run Scraper](04-Run_Scraper.md)

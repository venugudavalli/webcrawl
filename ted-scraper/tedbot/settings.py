BOT_NAME = 'TEDBot'

SPIDER_MODULES = ['tedbot.spiders']

AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = {
    'tedbot.pipelines.TimingsDownloaderPipeline': 100,
    'tedbot.pipelines.TranscriptDownloaderPipeline': 100,
    'tedbot.pipelines.MongoPipeline': 200,
}

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'ted'

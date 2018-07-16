import json
import scrapy

from http import HTTPStatus

import logging
import pymongo

def get_or_create_database(client, db_name):
    try:
        return next(x for x in client.ReadDatabases()
                    if x['id'] == db_name)
    except StopIteration:
        return client.CreateDatabase({'id': self.db_name})


def get_or_create_collection(client, db, coll_name):
    try:
        return next(x for x in client.ReadCollections(db['_self'])
                    if x['id'] == coll_name)
    except StopIteration:
        return client.CreateCollection(db['_self'], {'id': coll_name})


    
class MongoPipeline(object):
    #default_db_name = 'ted'
    collection_name = 'talks'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        
        #self.client = document_client.DocumentClient(self.endpoint,
        #                                            {'masterKey': self.key})
        #self.db = get_or_create_database(self.client, self.db_name)
        #self.collection = get_or_create_collection(self.client, self.db,
        #                                           self.coll_name)
    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()
        
    def process_item(self, item, spider):
        #self.client.UpsertDocument(self.collection['_self'], item)
        ## how to handle each post
        self.db[self.collection_name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item

class TimingsDownloaderPipeline(object):
    timings_url = 'https://hls.ted.com/talks/{}.json'

    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_item(self, item, spider):
        request = scrapy.Request(self.timings_url.format(item['id']))
        dfd = spider.crawler.engine.download(request, spider)
        dfd.addBoth(self.return_item, item)
        return dfd

    def return_item(self, response, item):
        if response.status != HTTPStatus.OK:
            return item
        timings = json.loads(response.text)
        item['timings'] = timings['timing']
        return item


class TranscriptDownloaderPipeline(object):
    transcript_url = 'https://www.ted.com/talks/{}/transcript.json'

    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_item(self, item, spider):
        request = scrapy.Request(self.transcript_url.format(item['id']))
        dfd = spider.crawler.engine.download(request, spider)
        dfd.addBoth(self.return_item, item)
        return dfd

    def return_item(self, response, item):
        if response.status != HTTPStatus.OK:
            return item
        transcript = json.loads(response.text)
        item['transcript'] = [lines
                              for x in transcript['paragraphs']
                              for lines in x['cues']]
        return item

# -*- coding: utf-8 -*-
import threading

from univider.logger import Logger


class Subprocessor():

    logger = Logger(__name__).getlogger()

    def __init__(self,params,result):
        self.key = params['uuid']
        self.url = params['url']
        if(result.has_key('title')):
            self.title = result['title']
        else:
            self.title = None
        if(result.has_key('html')):
            self.content = result['html']
        else:
            self.content = None

    def store(self):
        from univider.storager import Storager
        storager = Storager()
        storager.save(self.key,self.url,self.title,self.content)
        self.logger.info("stored " + self.url)

    def index(self):
        from univider.indexer import Indexer
        indexer = Indexer()
        indexer.save(self.key,self.url,self.title,self.content)
        self.logger.info("indexed " + self.url)

    def persist(self):
        threads = []
        t1 = threading.Thread(target=self.store)
        threads.append(t1)
        t2 = threading.Thread(target=self.index)
        threads.append(t2)

        for t in threads:
            t.setDaemon(True)
            t.start()
        # t.join()




# -*- coding: utf-8 -*-

from rediscluster import StrictRedisCluster

from univider.logger import Logger
from univider.settings import redis_nodes, redis_expires


class Cacher:

    logger = Logger(__name__).getlogger()

    redisconn = StrictRedisCluster(startup_nodes=redis_nodes,max_connections=10000)

    def set(self,key,value,expires = redis_expires):
        try:
            self.redisconn.set(key,value,expires)
            # redisconn.set('name','admin',5)
            # redisconn.set('age',18,5)
            # print "name is: ", redisconn.get('name')
            # print "age  is: ", redisconn.get('age')
        except Exception,e:
            self.logger.error("Redis Error!")

    def get(self,key):
        return self.redisconn.get(key)



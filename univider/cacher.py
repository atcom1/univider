#coding=utf-8
from rediscluster import StrictRedisCluster

class Cacher:

    redis_nodes =  [{'host':'10.78.155.61','port':16340},
                    {'host':'10.78.155.67','port':16340},
                    {'host':'10.78.155.68','port':16340},
                    {'host':'10.78.155.70','port':16340},
                    {'host':'10.78.155.71','port':16340},
                    {'host':'10.78.155.72','port':16340},
                   ]

    # redis_nodes =  [{'host':'192.168.136.130','port':7000},
    #                 {'host':'192.168.136.130','port':7001},
    #                 {'host':'192.168.136.130','port':7002},
    #                 {'host':'192.168.136.131','port':7000},
    #                 {'host':'192.168.136.131','port':7001},
    #                 {'host':'192.168.136.131','port':7002},
    #                ]

    redisconn = StrictRedisCluster(startup_nodes=redis_nodes)

    def set(self,key,value,expires = 86400):
        try:
            self.redisconn.set(key,value,expires)
            # redisconn.set('name','admin',5)
            # redisconn.set('age',18,5)
            # print "name is: ", redisconn.get('name')
            # print "age  is: ", redisconn.get('age')
        except Exception,e:
            print "Redis Error!"

    def get(self,key):
        return self.redisconn.get(key)



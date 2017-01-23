from rediscluster import StrictRedisCluster
import sys

def redis_cluster():
    # redis_nodes =  [{'host':'10.78.155.61','port':16340},
    #                 {'host':'10.78.155.67','port':16340},
    #                 {'host':'10.78.155.68','port':16340},
    #                 {'host':'10.78.155.70','port':16340},
    #                 {'host':'10.78.155.71','port':16340},
    #                 {'host':'10.78.155.72','port':16340},
    #                ]
    redis_nodes =  [{'host':'master.hadoop','port':6379}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    redisconn.set('name','admin')
    redisconn.set('age',18)
    print "name is: ", redisconn.get('name')
    print "age  is: ", redisconn.get('age')

redis_cluster()
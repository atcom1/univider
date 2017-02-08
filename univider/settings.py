# -*- coding: utf-8 -*-
import socket

if socket.gethostname() == 'EGG-PC':
    PROFILE = 'dev'
else:
    PROFILE = 'prod'

if PROFILE == 'dev':
    redis_nodes =  [{'host':'192.168.136.130','port':7000},
                    {'host':'192.168.136.130','port':7001},
                    {'host':'192.168.136.130','port':7002},
                    {'host':'192.168.136.131','port':7000},
                    {'host':'192.168.136.131','port':7001},
                    {'host':'192.168.136.131','port':7002},
                    ]
    redis_expires = 30
    hbase_host = 'master.hadoop'
    hbase_port = 9090

elif PROFILE == 'prod':
    redis_nodes =  [{'host':'10.78.155.61','port':16340},
                    {'host':'10.78.155.67','port':16340},
                    {'host':'10.78.155.68','port':16340},
                    {'host':'10.78.155.70','port':16340},
                    {'host':'10.78.155.71','port':16340},
                    {'host':'10.78.155.72','port':16340},
                    ]
    redis_expires = 86400
    hbase_host = '10.78.138.74'
    hbase_port = 9090
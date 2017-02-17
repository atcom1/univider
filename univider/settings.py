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
    persist = False
    hbase_host = 'master.hadoop'
    hbase_port = 9090
    es_host = ["master.hadoop"]

elif PROFILE == 'prod':
    redis_nodes =  [{'host':'10.78.155.61','port':16340},
                    {'host':'10.78.155.67','port':16340},
                    {'host':'10.78.155.68','port':16340},
                    {'host':'10.78.155.70','port':16340},
                    {'host':'10.78.155.71','port':16340},
                    {'host':'10.78.155.72','port':16340},
                    ]
    redis_expires = 86400
    persist = False
    hbase_host = '10.78.138.74'
    hbase_port = 9090
    es_host = ["10.78.138.53",
               "10.78.138.54",
               "10.78.138.55",
               "10.78.138.56",
               "10.78.138.57",
               "10.78.138.58",
               "10.78.138.59",
               "10.78.138.60",
               "10.78.138.61",
               "10.78.138.62",
               "10.78.138.63",
               "10.78.138.64",
               "10.78.138.65",
               "10.78.138.66",
               "10.78.138.67",
               "10.78.138.68",
               "10.78.138.69",
               "10.78.138.70",
               "10.78.138.71",
               "10.78.138.72",
               ]

#coding=utf-8

import sys
import os

from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

gen_py_path = os.path.abspath('gen-py')
sys.path.append(gen_py_path)
from hbase import THBaseService
from hbase.ttypes import *

class Storager:

    # create_namespace 'spider'
    # create 'spider:cplatform', {NAME => 'w', VERSIONS => 1, TTL => 2592000, BLOCKCACHE => true}

    host = "master.hadoop"
    port = 9090
    framed = False

    def save(self,key,url,title,content):

        socket = TSocket.TSocket(self.host, self.port)
        if self.framed:
          transport = TTransport.TFramedTransport(socket)
        else:
          transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = THBaseService.Client(protocol)

        transport.open()

        table = "spider:cplatform"

        put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="u",value=url)])
        client.put(table, put)
        put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="t",value=title)])
        client.put(table, put)
        put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="c",value=content)])
        client.put(table, put)
        # print "Putting:", put

        transport.close()

    def read(self,key):

        socket = TSocket.TSocket(self.host, self.port)
        if self.framed:
          transport = TTransport.TFramedTransport(socket)
        else:
          transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = THBaseService.Client(protocol)

        transport.open()

        table = "spider:cplatform"

        get = TGet(row=key)
        print "Getting:", get
        result = client.get(table, get)

        print "Result:", result

        transport.close()
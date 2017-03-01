# -*- coding: utf-8 -*-

import sys
import os

from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

from univider.settings import hbase_host, hbase_port, accessid, accesskey

gen_py_path = os.path.dirname(__file__) + '/gen-py'
sys.path.append(gen_py_path)
# from hbase import THBaseService
from hbase import THBaseService4CMH
from hbase.ttypes import *

class Storager:

    # create_namespace 'spider'
    # create 'spider:cplatform', {NAME => 'w', VERSIONS => 1, TTL => 2592000, BLOCKCACHE => true}

    host = hbase_host
    port = hbase_port
    framed = False

    def save(self,key,url,title,content):

        socket = TSocket.TSocket(self.host, self.port)
        if self.framed:
            transport = TTransport.TFramedTransport(socket)
        else:
            transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        # client = THBaseService.Client(protocol)
        client = THBaseService4CMH.Client(protocol)

        transport.open()

        table = "spider:cplatform"
        if(url != None and url != ''  ):
            put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="u",value=url)])
            client.put(table, put, accessid, accesskey)
        if(title != None and title != ''  ):
            try:
                put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="t",value=title)])
                client.put(table, put, accessid, accesskey)
            except UnicodeEncodeError,e:
                put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="t",value=title.encode('utf8'))])
                client.put(table, put, accessid, accesskey)

        if(content != None and content != ''  ):
            try:
                put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="c",value=content)])
                client.put(table, put, accessid, accesskey)
            except UnicodeEncodeError,e:
                put = TPut(row=key, columnValues=[TColumnValue(family="w",qualifier="c",value=content.encode('utf8'))])
                client.put(table, put, accessid, accesskey)

        # print "Putting:", put

        transport.close()

    def read(self,key):

        socket = TSocket.TSocket(self.host, self.port)
        if self.framed:
            transport = TTransport.TFramedTransport(socket)
        else:
            transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        # client = THBaseService.Client(protocol)
        client = THBaseService4CMH.Client(protocol)

        transport.open()

        table = "spider:cplatform"

        get = TGet(row=key)
        print "Getting:", get
        result = client.get(table, get, accessid, accesskey)

        print "Result:", result

        transport.close()
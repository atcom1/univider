#coding=utf-8
import threading
from time import sleep


class Subprocessor():

    def __init__(self,result):
        self.result = result

    def store(self):
        for i in range(100):
            print "aaaaa"
            sleep(1)

    def index(self):
        for i in range(100):
            print "bbbbb"
            sleep(3)

    def handle_result(self):
        threads = []
        t1 = threading.Thread(target=self.store)
        threads.append(t1)
        t2 = threading.Thread(target=self.index)
        threads.append(t2)

        for t in threads:
            t.setDaemon(True)
            t.start()




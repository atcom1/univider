#coding=utf-8
from univider.storager import Storager

storager = Storager()

# storager.save('aaaaa','http://www.baidu.com','百度','啦啦啦啦啦啦这是内容')

print storager.read('aaaaa')


#coding=utf-8
from univider.storager import Storager

storager = Storager()

# storager.save('aaaaa','http://www.baidu.com','百度','啦啦啦啦啦啦这是内容')

# print storager.read('aaaaa')
result =  storager.read('4462a2fe-8d4a-4f23-bb66-ec2b5b8174f56')
print result



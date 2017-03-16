# -*- coding: utf-8 -*-
import socket
import urllib2
import urlparse

from univider.logger import Logger

class Fetcher():

    logger = Logger(__name__).getlogger()

    def persist(self,params,result):

        try:
            from univider.settings import landing
            if(landing):
                from univider.subprocessor import Subprocessor
                subprocessor = Subprocessor(landing,params,result)
                subprocessor.persist()
            else:
                pass
        except Exception,e:
            print Exception,":",e

    def fetch_page_with_cache(self,params):
        if(params.has_key("iscache") and params["iscache"] == "false"):
            iscache = False
        else:
            iscache = True

        if(iscache):
            # params_c = params.copy()
            # del params_c['uuid']
            from univider.encrypter import get_md5_value
            ckey = get_md5_value(params['url'])
            try:
                from univider.cacher import Cacher
                cacher = Cacher()
                cvalue = cacher.get(ckey)
                if(cvalue!= 'null' and cvalue!= None and cvalue!=''):
                    self.logger.info('got cache ' + params['url'])
                    result = eval(cvalue)
                    # self.persist(params,result)
                    return result
            except Exception,e:
                print Exception,":",e
        result = self.fetch_page(params)
        self.logger.info('fetched source ' + params['url'])
        if(iscache):
            cacher.set(ckey,result)
            self.logger.info('cached source ' + params['url'])
        self.persist(params,result)
        return result

    def fetch_page(self,params):

        uuid = params["uuid"]
        node = socket.gethostname()

        try:
            url = params["url"]
            if(params.has_key("headers")):
                headers = urlparse.parse_qs(params["headers"], False)
            else:
                headers = {}

            if(params.has_key("method") and params["method"] == "POST"):
                # POST
                if(params.has_key("post.params")):
                    data = params["post.params"]
                else:
                    data = None
                req = urllib2.Request(url=url, data=data, headers=headers)
            else:
                # GET
                req = urllib2.Request(url=url, headers=headers)

            response = urllib2.urlopen(req,timeout=5)
            httpstatus = response.code
            httpcontenttype = response.info().getheader("Content-Type")

            if(params.has_key("ajax") and params["ajax"] == "true"):
                if(params.has_key("ajaxTimeout")):
                    ajaxTimeout = params["ajaxTimeout"]
                else:
                    ajaxTimeout = 8
                if(params.has_key("ajaxLoadImage")):
                    ajaxLoadImage = params["ajaxLoadImage"]
                else:
                    ajaxLoadImage = "false"
                from univider.render import Render
                render = Render()
                html = render.getDom(url,ajaxLoadImage,ajaxTimeout)
            else:
                html = response.read()
                if('GBK' in httpcontenttype or 'gbk' in httpcontenttype):
                    try:
                        html = html.decode('gbk')
                    except Exception,e:
                        print Exception,":",e

            # print 'html : ' + html

            try:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(html,'lxml')
                title = soup.title.string
            except Exception,e:
                print Exception,":",e
                title = ""
            status = "OK"

            # print 'title : ' + title

        except Exception,e:
            httpstatus = 400
            httpcontenttype = ""
            title = ""
            html = ""
            status = str(Exception)+" : "+str(e)
            print Exception,":",e


        if(params.has_key("onlytitle") and params["onlytitle"] == "true"):
            result = {
                'uuid':uuid,
                'status':status,
                'node':node,
                'httpstatus':httpstatus,
                'httpcontenttype':httpcontenttype,
                'title':title
            }
        else:
            result = {
                'uuid':uuid,
                'status':status,
                'node':node,
                'httpstatus':httpstatus,
                'httpcontenttype':httpcontenttype,
                'html':html,
            }

        return result
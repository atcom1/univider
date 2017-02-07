#coding=utf-8
import socket
import urllib2
import urlparse

from bs4 import BeautifulSoup

from univider.cacher import Cacher
from univider.encrypter import get_md5_value


class Fetcher():

    def fetch_page_with_cache(self,params):
        if(params.has_key("iscache") and params["iscache"] == "false"):
            iscache = False
        else:
            iscache = True
            params_c = params.copy()
            del params_c['uuid']
            ckey = get_md5_value(str(params_c))
            cacher = Cacher()
            cvalue = cacher.get(ckey)

        if(iscache):
            if(cvalue!= 'null' and cvalue!= None and cvalue!=''):
                print 'from cache'
                return eval(cvalue)
        print 'from source'
        cvalue = self.fetch_page(params)
        if(iscache):
            cacher.set(ckey,cvalue)
            # from univider.subprocessor import Subprocessor
            # subprocessor = Subprocessor()
            # subprocessor.handle_result(cvalue)
        return cvalue

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
                if('gbk' in html):
                    try:
                        html = html.decode('gbk')
                    except:
                        pass

            # print html

            try:
                soup = BeautifulSoup(html)
                title = soup.title.string
            except Exception:
                title = ""
            status = "OK"

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
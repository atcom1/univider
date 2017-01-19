#coding=utf-8
import socket
import urllib2
import urlparse

from bs4 import BeautifulSoup


def fetch_page(params):

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
        html = response.read()
        # print html
        soup = BeautifulSoup(html)
        title = soup.title.string
        status = "OK"

    except Exception,e:
        httpstatus = 400
        httpcontenttype = ""
        title = ""
        html = ""
        status = str(Exception)+" : "+str(e)
        print Exception,":",e


    if(params.has_key("onlytitle") and ( params["onlytitle"] == "true" or params["onlytitle"] == True )):
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
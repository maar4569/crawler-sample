# -*- coding: utf-8 -*-

from __future__ import with_statement
import re
import requests
from bs4 import BeautifulSoup

class UrlScrayper:
    def __init__(self):
        self._relatedurl = []
        self.__pages       = 0
        self.__currentpage = 1
    def target(self,targeturl):
        self._targeturl = targeturl

    def do(self):
        raise "abstract method"

class GoogSearchScrayper(UrlScrayper):

    def do(self):
        try:
            res =requests.get(self._targeturl)
            soup = BeautifulSoup(res.content , "html.parser")
            results = soup.findAll("h3", {'class':'r'})
            for link in results:
                related_url   = lambda val: re.sub(r'^/url\?\q\=','',val)
                self._relatedurl.append( related_url(link.a['href'].split('&')[0]) )
            return 0

        except Exception as e:
            raise Exception('exception in do()',e )

    def getRelatedUrl(self):
        return self._relatedurl

if __name__ == "__main__":

    print u"main start!" 
    url = 'https://www.google.co.jp/search?q=ruby'
    scrapyer = GoogSearchScrayper()
    scrapyer.target(url)
    scrapyer.do()
    ret = scrapyer.getRelatedUrl()
    print ret
#/url?q=http://openbook4.me/projects/92/sections/485&sa=U&ved=0ahUKEwjN_9vT_qbKAhXCsJQKHeSDDxwQFgheMAs&usg=AFQjCNGQxm01U8PM-FgQVV6iE1IQOEB2jA


    print u"main finished"





# -*- coding: utf-8 -*-

from __future__ import with_statement
import re
import requests
import outputwriter
from bs4 import BeautifulSoup

class UrlScrapyer:
    def __init__(self):
        self._targeturl = ""
        self._relatedurl = []
        self.__pages       = 0
        self.__currentpage = 1
    def target(self,targeturl):
        self._targeturl = targeturl

    def do(self):
        #raise "abstract method"
        raise NotImplementedError()

    def output(self,filename):
        try:
            ow = outputwriter.List2File()
            print len(self._relatedurl)
            ret = ow.output(filename,self._relatedurl)
            return 0
        except Exception as e:
            raise Exception(e)
class GoogSearchScrapyer(UrlScrapyer):
    def do(self):
        related_url   = lambda val: re.sub(r'^/url\?\q\=','',val)
        try:
            #related_url   = lambda val: re.sub(r'^/url\?\q\=','',val)
            res =requests.get(self._targeturl)
            res.raise_for_status()
            soup = BeautifulSoup(res.content , "html.parser")
            results = soup.findAll("h3", {'class':'r'})
            for link in results:
                self._relatedurl.append( related_url(link.a['href'].split('&')[0]) )
            return 0
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def getRelatedUrl(self):
        return self._relatedurl


    def __iter__(self):
        for url in self._relatedurl:
            yield url


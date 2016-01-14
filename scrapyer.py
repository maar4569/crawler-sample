# -*- coding: utf-8 -*-

from __future__ import with_statement
import re
import requests
from bs4 import BeautifulSoup

class UrlScrapyer:
    def __init__(self):
        self._relatedurl = []
        self.__pages       = 0
        self.__currentpage = 1
    def target(self,targeturl):
        self._targeturl = targeturl

    def do(self):
        raise "abstract method"

class GoogSearchScrapyer(UrlScrapyer):
    def do(self):
        try:
            res =requests.get(self._targeturl)
            res.raise_for_status()
            soup = BeautifulSoup(res.content , "html.parser")
            results = soup.findAll("h3", {'class':'r'})
            for link in results:
                related_url   = lambda val: re.sub(r'^/url\?\q\=','',val)
                self._relatedurl.append( related_url(link.a['href'].split('&')[0]) )
            return 0
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def getRelatedUrl(self):
        return self._relatedurl





# -*- coding: utf-8 -*-

from __future__ import with_statement
import re
import requests
import outputwriter
from bs4 import BeautifulSoup
#import log
from crawler.utils import log
import types
import sys
class UrlScrapyer:
    def __init__(self):
        self._targeturl = ""
        self._relatedurl = []
        self.__pages       = 0
        self.__currentpage = 1
        self._mylog = log.myLogger(self.__class__.__name__)
    def target(self,targeturl):
        self._targeturl = targeturl

    def do(self):
        #raise "abstract method"
        raise NotImplementedError()

    def output(self,filename):
        try:
            ow = outputwriter.List2File()
            ret = ow.output(filename,self._relatedurl)
            return 0
        except Exception as e:
            raise Exception(e)
class GoogSearchScrapyer(UrlScrapyer):
    def do(self):
        """ scraping Urls from a first result page in google search.
        when given target url(into textbox with 'related:'), and return related urls.

        return:
            normally 0 , abnormally raise Exception.

        """
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
            if isinstance(e.message,requests.packages.urllib3.exceptions.SSLError):
                msg = e.message.message.message
            else:
                msg = e.message
            self._mylog.error(msg)
            methodname = sys._getframe(1).f_code.co_name
            raise Exception("raised exception. in " + self.__class__.__name__ + "." +  methodname + "()")

    def getRelatedUrl(self):
        return self._relatedurl


    def __iter__(self):
        for url in self._relatedurl:
            yield url


# -*- coding: utf-8 -*-

class RelatedSite:

    def __init__(self,srcurl):
        self._srcurl=srcurl
        self._results=[]
        #self._last   = 0
        self._iter     = iter(self._results)

    def length(self):
        return len(self._results)

    def srcurl(self):
        return self._srcurl

    def append(self,url):
        self._results.append(url)

    def next(self):
        try:
            return self._iter.next()
        except StopIteration :
            raise StopIteration()

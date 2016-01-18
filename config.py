# -*- coding: utf-8 -*-
import yaml

class CrawlerConfig(object):
    def __init__(self,filename):
        self._config   = {}
        self._fo = open(filename,'r')
        
    def load(self):
        try:
            self._config   = yaml.load(self._fo)
            self._fo.close()
            return self._config

        except Exception as e:
            print e
            self._fo.close()
            raise Exception


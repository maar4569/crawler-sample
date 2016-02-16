# -*- coding: utf-8 -*-
import log
class Scoreler(object):
    def __init__(self):
        self._relatedsite = {}
        self._mylog = log.myLogger(self.__class__.__name__)

    def setData(self,categorized_relatedsite):
        self._relatedsite = categorized_relatedsite

    def analyze(self):
        #raise Exception('abstract method.')
        raise NotImplementedError()

class StdScoreler(Scoreler):
    """return a scored category.analyze which category the relatedsites belong to.
           args: Scoreler object

           return caregory name


    """
    def analyze(self):
        """ analyze a category of a target url.
            
                return : category name
        """ 
        stats = {}
        try:
            majorCategory= ""
            majorScore   = 0
            if len(self._relatedsite) == 0 : return -1
            for url,cat in self._relatedsite.items():
                if not stats.has_key(cat):
                    stats[cat]=1
                else:
                    stats[cat]=stats[cat]+1
            majorCategory = max(stats.items(), key=lambda x:x[1])[0]
            majorScore    = max(stats.items(), key=lambda x:x[1])[1]
            return majorCategory
        except Exception as e:
            self._mylog.error(e.message)
            raise Exception(e)


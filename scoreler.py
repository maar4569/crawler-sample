# -*- coding: utf-8 -*-

class Scoreler:
    def __init__(self):
        self._relatedsite = {}

    def setData(self,categorized_relatedsite):
        self._relatedsite = categorized_relatedsite

    def analyze(self):
        #raise Exception('abstract method.')
        raise NotImplementedError()

class StdScoreler(Scoreler):
    """return a scored category.analyze which category the relatedsites belong to.
           args: Scoreler object

           return caregoryname


    """
    def analyze(self):
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
            raise Exception(e)

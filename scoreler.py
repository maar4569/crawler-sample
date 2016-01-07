# -*- coding: utf-8 -*-

import json
class Scoreler:
    def __init__(self,categorized_relatedsite):
        self._relatedsite = categorized_relatedsite

    def analyze(self):
        raise Exception('abstract method.')

class StdScoreler(Scoreler):
    #return a scored category.analyze which category the relatedsites belong to.
    def analyze(self):
        stats = {}
        try:
            sites_len = len(self._relatedsite)
            for url,cat in self._relatedsite.items():
                stats[cat] = 1 not if self._relatedsite.has_key(cat) else stats[cat]=stats[cat]+1
            majorCategory = max(stats.items(), key=lambda x:x[1])[0]
            majorScore    = max(stats.items(), key=lambda x:x[1])[1]

            return majorCategory
        except:
            raise Exception('exception in do()')

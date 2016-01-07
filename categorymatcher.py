# -*- coding: utf-8 -*-
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
                if not self._relatedsite.has_key(cat):
                    stats[cat] = 1
                else:
                    stats[cat] = stats[cat]+1
            
            return u'Weather'
        except:
            raise Exception('exception in do()')


class CategorySetter(self):
    def _init__(self,exepath):
        self_.exepath =exepath
    def do(self):
        raise Exception('abstract method.')

class CategorySetterExe(CategorySetter)
    def do(self):
        try:
        #call exe
        except:
            raise Exception('exception in do()')

class CategorySetterAPI(CategorySetter)
    def do(self):
        try:
        #call api
        except:
            raise Exception('exception in do()')

#given non-categrized url to this method and return category
class CategoryValidator:
    def __init__(self,targeturl):
        self._targeturl = targeturl
        self._relatedsites = []       
        self._catgorized_sites = {}

    def do(self,scoreler,categorysetter):
        try:
            #overview
            #use webdb api directory or a file analyzed by webdb api.
            #return a category given to a non-categorized url.

            #detail
            #1.input a target url that is non-categorized.
            # check this constructor.

            #2.get relatedsites from a target url.
            # call scrapy

            #3.categorized relatedsites.(call exefile or call C++API)
            self._categorized_sites = categorysetter.do()
 
            #4.analyze categorized relatedsites.
            _category = scoreler.analyze()
            return _category

        except:
            raise Exception

    def getDetail(self):
        return self._categorized_sites

        #for example 
        {
            "results":
             [
                {"url":"sample01.com,"cat":"categoryA"},
                {"url":"sample02.com,"cat":"categoryB"},
                {"url":"sample03.com,"cat":"categoryV"},
                {"url":"sample04.com,"cat":"categoryA"}
              ]
        }



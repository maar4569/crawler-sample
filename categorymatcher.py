# -*- coding: utf-8 -*-
class CategorySetter:
    def __init__(self,exepath):
        self._exepath =exepath
        self._relatedurls = []
        self._categorized_url = {}

    def do(self):
        raise Exception('abstract method.')

    def setData(relatedurls):
        self._relatedurls = relatedurls
        
    def items(self):
        return self._categorized_url

class CategorySetterExe(CategorySetter):
    def do(self):
        try:
        #call exe (write file)
        #subprocess category.exe
        #open file defined categorized urls
        #sample http://domain.com,"news"
            print "success"      
        except Exception as e:
            raise Exception(e.args)

class CategorySetterAPI(CategorySetter):
    def do(self):
        try:
            print "success"      
        #call api
        except Exception as e:
            raise Exception(e.args)

#given non-categrized url to this method and return category
class CategoryValidator:
    def __init__(self,targeturl):
        self._targeturl = targeturl
        self._relatedsites = []       
        self._catgorized_sites = {}

    def do(self,scrapyer,scoreler,categorysetter):
        try:
            self._relatedsites = []       
            self._catgorized_sites = {}
            #overview
            #use webdb api directory or a file analyzed by webdb api.
            #return a category given to a non-categorized url.

            #detail
            #1.get relatedsites(list) from a target url.
            # call scrapy
            scrapyer.target(targeturl)
            ret = scrapyer.do()
            self._relatedsites = scrapyer.getRelatedUrl()

            #2.categorized relatedsites.(call exefile or call C++API)
            categorysetter.setData(self._relatedsites)
            self._categorized_sites = categorysetter.do()
 
            #3.analyze categorized relatedsites.
            scoreler.setData(self._categorized_sites)
            _category = scoreler.analyze()
            return _category

        except:
            raise Exception

    def getDetail(self):
        return self._categorized_sites

        #for example 
        #{
        #    "results":
        #     [
        #        {"url":"sample01.com,"cat":"categoryA"},
        #        {"url":"sample02.com,"cat":"categoryB"},
        #        {"url":"sample03.com,"cat":"categoryV"},
        #        {"url":"sample04.com,"cat":"categoryA"}
        #      ]
        #}



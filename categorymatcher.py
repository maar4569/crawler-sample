# -*- coding: utf-8 -*-
import re
import callprocess
class CategorySetter:
    def __init__(self,exepath,inputfile,outputfile):
        self._exepath =exepath
        self._inputfile = inputfile
        self._outputfile = outputfile
        self._relatedurls = []
        self._categorized_url = {}
        self._rm_quoat   = lambda val: re.sub(r'\"','',val)
    def do(self):      
        raise Exception('abstract method.')

    def setData(self,relatedurls):
        self._relatedurls = relatedurls
 
    def _getCategorizedUrls(self): 
        rm_quoat   = lambda val: re.sub(r'\"','',val)
        try:
            with open(self._outputfile) as fo:
                for l in fo:
                    url      = self._rm_quoat(l.split(",")[0].strip())
                    category = self._rm_quoat(l.split(",")[1].strip())
                    self._categorized_url[url] = category
                return 0
        except Exception as e:
            raise Exception(e.args)

    def items(self):
        return self._categorized_url       

class CategorySetterExe(CategorySetter):
    def do(self):
        try:
            #call exe (write file)a
            #subprocess category.exe
            ret = callprocess.callhoge(self._exepath,self._inputfile,self._outputfile)
            
            #open file defined categorized urls
            #sample http://domain.com,"news"
            ret = self._getCategorizedUrls()

            return ret
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
            scrapyer.target(self._targeturl)
            ret = scrapyer.do()
            self._relatedsites = scrapyer.getRelatedUrl()


            #2.categorized relatedsites.(call exefile or call C++API)
            categorysetter.setData(self._relatedsites)
            ret  = categorysetter.do()
            self._categorized_sites = categorysetter.items()

            #3.analyze categorized relatedsites.
            scoreler.setData(self._categorized_sites)
            _category = scoreler.analyze()
            return _category

        except Exception as e:
            raise Exception(e.args) 

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



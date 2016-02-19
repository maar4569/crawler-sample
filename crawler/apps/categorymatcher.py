# -*- coding: utf-8 -*-
import re
from crawler.apps import callprocess
from crawler.utils import log
import sys
class CategorySetter(object):
    #def __init__(self):
    def __init__(self,exepath,inputfile,outputfile):
        self._exepath =exepath
        self._inputfile = inputfile
        self._outputfile = outputfile
        self._relatedurls = []
        self._categorized_url = {}
        self._rm_quoat   = lambda val: re.sub(r'\"','',val)
        self._mylog = log.myLogger(self.__class__.__name__)
    def do(self):      
        raise Exception('abstract method.')

    def setData(self,relatedurls):
        self._relatedurls = relatedurls
 
    def _getCategorizedUrls(self):
        print "call _getCategorizedUrls" + self._outputfile
        rm_quoat   = lambda val: re.sub(r'\"','',val)
        try:
            with open(self._outputfile) as fo:
                for l in fo:
                    url      = self._rm_quoat(l.split(",")[0].strip())
                    category = self._rm_quoat(l.split(",")[1].strip())
                    self._categorized_url[url] = category
                return 0
        except Exception as e:
            self._mylog.error(" outputfile:" + self._outputfile)
            raise Exception(e.args)

    def items(self):
        return self._categorized_url       

class CategorySetterExe(CategorySetter):
    """set category with CLI application.
       CLI application  given urllist  , return categorized urllist.
    """
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
            self._mylog.error("inputfile:" + self._inputfile +  " outputfile:" + self._outputfile)
            raise Exception(e.args)

class CategorySetterAPI(CategorySetter):
    def do(self,relatedurls):
        try:
            self._relatedurls = relatedurls
            print "success"      
        #call api
        except Exception as e:
            raise Exception(e.args)

#given non-categrized url to this method and return category
class CategoryValidator(object):
    """ validate non-categorized url , and given it to a category.
        public attributes:
        - none
        public method:
        - do: validate non-categorized url , and return it.
        - getDetail: return Urls related to  non-categorized url.
    """
    def __init__(self,targeturl,transaction_name):
        self._targeturl = targeturl
        self._relatedsites = []       
        self._categorized_sites = {}
        self._transaction_name = transaction_name
        self._category_name= ''
        self._mylog = log.myLogger(self.__class__.__name__)
    def do(self,scrapyer,scoreler,categorysetter):
        """ validate non-categorized url
        args:
            scrapyer : scrapyer object.
            scoreler : scoreler object.
            categorysetter : categorysetter object.

        return:
            if normally ,return a category(strings)
            if abnormally ,raise Exception
        """
        try:
            self._relatedsites = []       
            self._categorized_sites = {}
            #overview
            #use webdb api directory or a file analyzed by webdb api.
            #return a category given to a non-categorized url.

            #detail
            #1.get relatedsites(list) from a target url and output csv
            # call scrapy
            self._mylog.info('search this URL =>' + self._targeturl)
            scrapyer.target(self._targeturl)
            ret = scrapyer.do()
            scrapedURLfile = self._transaction_name + ".scraped"
            ret = scrapyer.output(scrapedURLfile)
            self._relatedsites = scrapyer.getRelatedUrl()


            #2.categorized relatedsites.(call exefile or call C++API)
            ret  = categorysetter.do()
            self._categorized_sites = categorysetter.items()
            self._mylog.info('set relatedURLs to category.')

            #3.analyze categorized relatedsites.
            scoreler.setData(self._categorized_sites)
            #_category = scoreler.analyze()
            #self._mylog.info('analyzed. [' + _category  + '] => ' + self._targeturl)
            self._category_name = scoreler.analyze()
            self._mylog.info('analyzed. [' + self._category_name  + '] => ' + self._targeturl)
            return self._category_name

        except Exception as e:
            self._mylog.error(e.message)
            raise Exception(e) 

    def getDetail(self):
        """ return urls related to a non-categorized url.
        these urls are categorized with a categorysetter object , 
        and contained in list.
        
        return:
             List of categorized urls. 
        """
        return self._categorized_sites




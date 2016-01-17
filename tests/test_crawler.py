# -*- coding: utf-8 -*-

import unittest
from categorymatcher import CategorySetterExe,CategoryValidator
from scrapyer import GoogSearchScrapyer
from scoreler import StdScoreler
import outputformatter as fmter
import contrib.JSONStreamWriter.JSONStreamWriter as JSONStreamWriter
import outputwriter
import re
from mock import Mock
import time
class TestCategoryValidator(unittest.TestCase):
    def setUp(self):
	self._url            = 'https://www.google.co.jp/search?q=ruby'
        self._transaction_id = "transaction_test"
        self._result_json    = "result.json"
        self._validator      = CategoryValidator(self._url,self._transaction_id)
        self._scrapyer       = GoogSearchScrapyer()
        self._scoreler       = StdScoreler()
        self._relatedurls    = ["https://python.com","https://javascript.com"]

        self._no_cat_url_list = "./tests/data/no_cat_url.txt"
        #categorysetterexe
        self._exepath = "ls"
        self._infile  = "./tests/data/" + self._transaction_id + "1.scraped"
        self._outfile = "./tests/data/" + self._transaction_id + "1.categorized"
        self._categorysetter = CategorySetterExe(self._exepath,self._infile,self._outfile)
        rm_quoat   = lambda val: re.sub(r'\"','',val)

    #success
    #use mock in all classes
    #one record
    def test_success_all_mock(self):
        #scraper mock
        self._scrapyer.target(self._url)
        self._scrapyer.do = Mock()
        self._scrapyer.do.return_value = 0
        self._scrapyer.getRelatedUrl = Mock()
        self._scrapyer.getRelatedUrl.return_value = self._relatedurls
        #scoreler mock
        self._scoreler.analyze = Mock()
        self._scoreler.analyze.return_value = "lang"

        #categorysetter mock
        self._categorysetter.do()
        category = self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)
        self.assertEqual(category,"lang")

        #outputjson
        evt = fmter.Urls2Json(self._url,category,self._validator.getDetail(),self._transaction_id)
        with JSONStreamWriter.ArrayWriter(self._result_json) as jstream:
            jstream.write(evt)
    #many records
    def test_success_all_mock_many_records(self):
        i=0
        with open(self._no_cat_url_list) as fo:
            with JSONStreamWriter.ArrayWriter(self._result_json) as jstream:
                for url in fo:
                    if url.strip()== "" : continue
                    print "transactionID=>" + str(time.time()).replace(".","_")
                    #scraper mock
                    self._scrapyer.target(url)
                    self._scrapyer.do = Mock()
                    self._scrapyer.do.return_value = 0
                    self._scrapyer.output = Mock()
                    self._scrapyer.output.return_value = 0
 
                    self._scrapyer.getRelatedUrl = Mock()
                    self._scrapyer.getRelatedUrl.return_value = self._relatedurls
                    
                    self._exepath = "ls"
                    fpath         = "./tests/data/"
                    self._infile  = fpath + self._transaction_id + str(i+1) + ".scraped"
                    self._outfile = fpath + self._transaction_id + str(i+1) + ".categorized"
                    self._categorysetter = CategorySetterExe(self._exepath,self._infile,self._outfile)
                    ret = self._categorysetter.do()
                     
                    wkValidator  = CategoryValidator(self._url,fpath + self._transaction_id + str(i))
                    #wkValidator  = CategoryValidator(self._url,self._transaction_id + str(i))
                    category = wkValidator.do(self._scrapyer,self._scoreler,self._categorysetter)

                    #outputjson
                    evt = fmter.Urls2Json(url,category,wkValidator.getDetail(),self._transaction_id)
                    jstream.write(evt)

                    
                    i=i+1

if __name__ == "__main__":
    unittest.main()

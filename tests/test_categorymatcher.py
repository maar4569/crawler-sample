# -*- coding: utf-8 -*-

import unittest
from categorymatcher import CategorySetterExe,CategoryValidator
from scrapyer import GoogSearchScrapyer
from scoreler import StdScoreler
import outputwriter
import re
from mock import Mock

class TestCategoryValidator(unittest.TestCase):
    def setUp(self):
	self._url = 'https://www.google.co.jp/search?q=ruby'
        self._transaction_id = "transaction_test"
        self._validator= CategoryValidator(self._url,self._transaction_id)
        self._scrapyer       = GoogSearchScrapyer()
        self._scoreler       = StdScoreler()

        self._relatedurls = ["https://facebook.com","https://instagram.com"]
        #categorysetterexe
        exepath = "ls"
        #self._infile  = "nocaturl.txt"
        self._infile  = self._transaction_id + ".scraped"
        self._outfile = "categorized_url.txt"
        self._categorysetter = CategorySetterExe(exepath,self._infile,self._outfile)
        #self._categorysetter = CategorySetterExe()
        rm_quoat   = lambda val: re.sub(r'\"','',val)

    def test_categorysetterexe(self):
        #set relatedurls(list)
        self._categorysetter.setData(self._relatedurls)
        self._categorysetter.do()
        categorized_urls = self._categorysetter.items()
        self.assertEqual(len(categorized_urls),4)
      
    #success
    #use mock in all classes
    def test_success_all_mock(self):
        #scraper mock
        self._scrapyer.target(self._url)
        self._scrapyer.do = Mock()
        self._scrapyer.do.return_value = 0
        self._scrapyer.getRelatedUrl = Mock()
        self._scrapyer.getRelatedUrl.return_value = self._relatedurls
        #scoreler mock
        self._scoreler.analyze = Mock()
        self._scoreler.analyze.return_value = "searchengine"

        #categorysetter mock
        self._categorysetter.setData(self._relatedurls)
        self._categorysetter.do()
        category = self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)
        self.assertEqual(category,"searchengine")

        #outputjson
        writer = outputwriter.Url2JsonWriter()
        writer.output(self._transaction_id +".json",self._validator.getDetail(),self._url)
        
    #use mock in scoreler and categorysetter 
    def test_success_scoreler_categorysetter_mock(self):
        #scrapyer real internet access.
        self._scrapyer.target(self._url)
        
        #scoreler mock
        self._scoreler.analyze = Mock()
        self._scoreler.analyze.return_value = "searchengine"

        #categorysetter mock
        self._categorysetter.do()
        category = self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)
        print self._validator.getDetail()
        self.assertEqual(category,"searchengine")

    #use mock in categorysetter 
    def test_success_categorysetter_mock(self):
        #scrapyer real internet access.
        self._scrapyer.target(self._url)

        #categorysetter mock
        self._categorysetter.do()
        category = self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)

        print self._validator.getDetail()
        self.assertEqual(category,"SNS")

    #error
    #use mock in all classes
    def test_error_categoryvalidator(self):
        #scraper mock cause exception
        self._scrapyer.target(self._url)
        self._scrapyer.do = Mock()
        self._scrapyer.do.side_effect = Exception
        self._scrapyer.getRelatedUrl = Mock()
        self._scrapyer.getRelatedUrl.return_value = self._relatedurls
        #scoreler mock
        self._scoreler.analyze = Mock()
        self._scoreler.analyze.return_value = "searchengine"

        #categorysetter mock
        self._categorysetter.setData(self._relatedurls)
        self._categorysetter.do()
        with self.assertRaises(Exception) as cnmgr:
            self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)
        print cnmgr.exception

    #use mock in scoreler and categorysetter 
    def test_error_categoryvalidator2(self):
        #scraper mock
        self._scrapyer.target(self._url)
        self._scrapyer.do = Mock()
        self._scrapyer.do.return_value = 0
        self._scrapyer.getRelatedUrl = Mock()
        self._scrapyer.getRelatedUrl.return_value = self._relatedurls
        #scoreler mock cause exception
        self._scoreler.analyze = Mock()
        self._scoreler.analyze.side_effect = Exception

        #categorysetter mock
        self._categorysetter.setData(self._relatedurls)
        self._categorysetter.do()
        with self.assertRaises(Exception) as cnmgr:
            self._validator.do(self._scrapyer,self._scoreler,self._categorysetter)
        print cnmgr.exception


   #def test_do_url_format_error(self):
    #	url = 'not_url_format'
    #    self._scrapyer.target(url)
    #    with self.assertRaises(Exception) as cnmgr:
    #        self._scrapyer.do()

    #    print cnmgr.exception

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-

import unittest
from categorymatcher import CategorySetterExe,CategoryValidator
from scrapyer import GoogSearchScrapyer
from scoreler import StdScoreler
import re
from mock import Mock

class TestCategoryValidator(unittest.TestCase):
    def setUp(self):
	self._url = 'https://www.google.co.jp/search?q=ruby'
        self._validator= CategoryValidator(self._url)
        self._scrapyer       = GoogSearchScrapyer()
        self._scoreler       = StdScoreler()

        #
        self._relatedurls = ["https://facebook.com","https://instagram.com"]
        #categorysetterexe
        exepath = "tool"
        self._infile  = "nocaturl.txt"
        self._outfile = "categorized_url.txt"
        self._categorysetter = CategorySetterExe(exepath,self._infile,self._outfile)
        rm_quoat   = lambda val: re.sub(r'\"','',val)

    def test_categorysetterexe(self):
        #set relatedurls(list)
        self._categorysetter.setData(self._relatedurls)
        self._categorysetter.do()
        categorized_urls = self._categorysetter.items()
        self.assertEqual(len(categorized_urls),3)
      
    #error
    def test_success_categoryvalidator(self):
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

 


   #def test_do_url_format_error(self):
    #	url = 'not_url_format'
    #    self._scrapyer.target(url)
    #    with self.assertRaises(Exception) as cnmgr:
    #        self._scrapyer.do()

    #    print cnmgr.exception

if __name__ == "__main__":
    unittest.main()

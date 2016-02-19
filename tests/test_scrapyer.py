# -*- coding: utf-8 -*-

import unittest
from crawler.apps import scrapyer
from crawler.apps import outputwriter
class TestGoogleSearchScrapyer(unittest.TestCase):
    def setUp(self):
	self._url = 'https://www.google.co.jp/search?q=ruby'
        self._scrapyer= scrapyer.GoogSearchScrapyer()
    #error
    def test_do_connection_error(self):
	url = 'https://dummy.com/status/404'
        self._scrapyer.target(url)
        with self.assertRaises(Exception) as cnmgr:
            self._scrapyer.do()
        print cnmgr.exception

    def test_do_url_format_error(self):
	url = 'not_url_format'
        self._scrapyer.target(url)
        with self.assertRaises(Exception) as cnmgr:
            self._scrapyer.do()

        print cnmgr.exception
    #success
    def test_do_success(self):
        self._scrapyer.target(self._url)
        ret=self._scrapyer.do()
        self.assertEquals(ret,0)

    def test_getRelatedUrl_success(self):
        self._scrapyer.target(self._url)
        ret=self._scrapyer.do()
        relatedUrl = self._scrapyer.getRelatedUrl()
        self.assertGreater(len(relatedUrl),0)

    def test_output_success(self):
        filename = "scrapyer_output_test.txt"
        self._scrapyer.target(self._url)
        ret=self._scrapyer.do()
        print self._scrapyer.getRelatedUrl()
        ret = self._scrapyer.output(filename)
        self.assertEqual(ret,0)

if __name__ == "__main__":
    unittest.main()

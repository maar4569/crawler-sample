# -*- coding: utf-8 -*-

import unittest
import scrapyer

class TestScrapyer(unittest.TestCase):
    def setUp(self):
	url = ' https ://www.google.co.jp/search?q=ruby'
        self._scrapyer= scrapyer.googSearchScrapyer(url)

    def test_do_connection_error(self):
        self._scrapyer.do()

    def test_do(self):
        ret= self._scrapyer.do()
        self.assertEquals(ret,0)

    def test_getRelatedUrl(self):
        relatedUrl = self._scrapter.getRelatedUrl()

if __name__ == "__main__":
    unittest.main()

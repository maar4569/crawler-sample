# -*- coding: utf-8 -*-

import unittest
from crawler.apps import relatedsite
from crawler.apps import scoreler


class TestScoreler(unittest.TestCase):
    def setUp(self):
        self._categorized_relsites = {}
        self._scoreler= scoreler.StdScoreler()

    #error
    def test_analyze_if_relsites_is_empty(self):
        category = self._scoreler.analyze()
        self.assertEqual(category,-1)

    #success
    def test_analyze(self):
        self._categorized_relsites["http://google.com"]="searchengine"
        self._categorized_relsites["http://facebook.com"]="SNS"
        self._categorized_relsites["http://instagram.com"]="SNS"
        self._categorized_relsites["http://amazon.com"]="retail"
        self._categorized_relsites["http://yahoo.com"]="portal"
        self._scoreler.setData(self._categorized_relsites)
        category = self._scoreler.analyze()
        self.assertEquals(category,"SNS")
    #success
    #take precedence with first in
    def test_analyze_if_same_value_exists(self):
        self._categorized_relsites["http://google.com"]="searchengine"
        self._categorized_relsites["http://yahoo.com"]="portal"
        self._categorized_relsites["http://yahoo.co.jp"]="portal"
        self._categorized_relsites["http://facebook.com"]="SNS"
        self._categorized_relsites["http://instagram.com"]="SNS"
        self._categorized_relsites["http://amazon.com"]="retail"
        self._scoreler.setData(self._categorized_relsites)
        category = self._scoreler.analyze()
        self.assertNotEquals(category,"SNS")


if __name__ == "__main__":
    unittest.main()

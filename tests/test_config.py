# -*- coding: utf-8 -*-
import unittest
from crawler.apps.config import CrawlerConfig
from crawler.config.crawlersetting import configureCrawler
class TestCrawlerConfig(unittest.TestCase):
    def setUp(self):
        #self._config = CrawlerConfig("./crawler/config/crawler.config")
        self._GLOBAL_SETTINGS = configureCrawler()

    #success
    #def test_success(self):
        #dictConf = self._config.load()
        #print dictConf
        #print dictConf["settings"]["outputjson"]
        #print dictConf["settings"]["exepath"]
        #self.assertTrue(dictConf)

    def test_success_2(self):
        print 'GLOBAL_SETTINGS'
        print self._GLOBAL_SETTINGS['directory']['transaction']
        self.assertTrue(self._GLOBAL_SETTINGS)

if __name__ == "__main__":
    unittest.main()

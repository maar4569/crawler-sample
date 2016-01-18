# -*- coding: utf-8 -*-
import unittest
from config import CrawlerConfig


class TestCrawlerConfig(unittest.TestCase):
    def setUp(self):
        self._config = CrawlerConfig("./crawler_config.yaml")

    #success
    def test_success(self):
        dictConf = self._config.load()
        print dictConf
        print dictConf["settings"]["outputjson"]
        print dictConf["settings"]["exepath"]
        self.assertTrue(dictConf)

if __name__ == "__main__":
    unittest.main()

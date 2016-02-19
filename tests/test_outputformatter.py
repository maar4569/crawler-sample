# -*- coding: utf-8 -*-

import unittest
import os
import json
import crawler.apps.outputformatter as fmter


class TestOutputFormatter(unittest.TestCase):
    def setUp(self):
        self._srcurl    = "http://mydomain.com"
        self._category  = "SNS"
        self._tid       = "12345"
        self._urls   = {}
        self._urls["http://www.instagram.com"] = "SNS"
        self._urls["http://www.facebook.com"] = "SNS"
        self._urls["http://www.twitter.com"] = "SNS"
    #success
    #should do this unittest to do validate json format  with a jsonschema package
    def test_success_jsonfmter(self):
        evt = fmter.Urls2Json(self._srcurl,self._category,self._urls,self._tid)
        print evt

    def test_success_jsonfmter_no_tid(self):
        evt = fmter.Urls2Json(self._srcurl,self._category,self._urls,"")
        self.assertEqual(evt["res"][0]["id"],-9999)

    #error lack of some parameters.
    def test_error_jsonfmter_no_tid_urls(self):
        self.assertRaises(Exception, lambda: fmter.Urls2Json(self._srcurl,self._category,"",""))

    def test_error_jsonfmter_no_tid_urls_and_category(self):
        self.assertRaises(Exception, lambda: fmter.Urls2Json(self._srcurl,"","",""))

    def test_error_jsonfmter_no_args(self):
        self.assertRaises(Exception, lambda: fmter.Urls2Json("","","",""))

if __name__ == "__main__":
    unittest.main()
